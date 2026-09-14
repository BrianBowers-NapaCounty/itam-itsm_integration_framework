"""Cherwell Service Management REST connector.

ADAPTER-SKELETON:
Authentication follows the documented /CherwellAPI/token OAuth2-style flow.
Record retrieval is intentionally centered on saved searches because Business
Object IDs and field IDs are installation-specific.
"""

from __future__ import annotations
import requests

from ..core.connector import ITSMConnector
from ..core.http import request_with_retry
from ..core.models import Ticket, Asset, HealthCheck, parse_datetime


class CherwellConnector(ITSMConnector):
    platform_name = "Cherwell"
    capabilities = frozenset({"tickets.read"})

    def __init__(self, *, base_url, client_id, username, password, auth_mode="Internal", incident_saved_search=""):
        self.base_url = base_url.rstrip("/")
        self.client_id = client_id
        self.incident_saved_search = incident_saved_search
        self.session = requests.Session()
        token_url = f"{self.base_url}/token"
        data = {"grant_type":"password","client_id":client_id,"username":username,"password":password}
        response = request_with_retry(
            self.session, "POST", token_url,
            params={"auth_mode":auth_mode, "api_key":client_id},
            data=data,
            headers={"Accept":"application/json"},
        )
        token = response.json()["access_token"]
        self.session.headers.update({"Authorization":f"Bearer {token}","Accept":"application/json"})

    def _api(self, tail):
        return f"{self.base_url}/api/V1/{tail.lstrip('/')}"

    def _request(self, method, tail, **kwargs):
        return request_with_retry(self.session, method, self._api(tail), **kwargs)

    def health_check(self):
        import time
        t0 = time.perf_counter()
        try:
            r = self._request("GET", "getsearchitems", params={"links":"false"})
            return HealthCheck(self.platform_name, r.ok, "Cherwell REST API reachable", (time.perf_counter()-t0)*1000)
        except Exception as exc:
            return HealthCheck(self.platform_name, False, f"{type(exc).__name__}: {exc}")

    def run_saved_search(self, search_name, *, association="Incident", scope="Global", scope_owner="(None)"):
        # Saved-search results are one of the most portable ways to demonstrate
        # Cherwell access without hard-coding Business Object/field IDs.
        tail = (
            f"getsearchresults/association/{association}/scope/{scope}/"
            f"scopeowner/{scope_owner}/searchname/{search_name}"
        )
        return self._request("GET", tail).json()

    @staticmethod
    def _field_map(record):
        # Search-result schemas depend on the saved search. Convert common
        # field/value collections to a case-insensitive dictionary.
        out = {}
        fields = record.get("fields") or record.get("Fields") or []
        for f in fields:
            name = str(f.get("name") or f.get("displayName") or f.get("fieldId") or "")
            out[name.lower()] = f.get("value") or f.get("displayValue") or ""
        return out

    def _ticket(self, r):
        f = self._field_map(r)
        rid = str(r.get("busObRecId") or r.get("recordId") or f.get("recid",""))
        public_id = str(r.get("busObPublicId") or f.get("incident id") or rid)
        return Ticket(
            id=rid, number=public_id,
            short_description=str(f.get("short description") or f.get("description","")),
            status=str(f.get("status","")), priority=str(f.get("priority","")),
            assignment_group=str(f.get("team") or f.get("owned by team","")),
            assignee=str(f.get("owned by","")), location_id=str(f.get("location","")),
            opened_at=parse_datetime(f.get("created date time")),
            updated_at=parse_datetime(f.get("last modified date time")),
            due_at=parse_datetime(f.get("sla resolve by")),
            source=self.platform_name, raw=r,
        )

    def iter_tickets(self, *, updated_since=None, limit=None, raw_filter=None):
        search = raw_filter or self.incident_saved_search
        if not search:
            raise ValueError("Configure cherwell.incident_saved_search or pass raw_filter=<saved search name>.")
        payload = self.run_saved_search(str(search))
        rows = payload.get("businessObjects") or payload.get("results") or []
        count = 0
        for r in rows:
            t = self._ticket(r)
            if updated_since and (not t.updated_at or t.updated_at < updated_since):
                continue
            yield t
            count += 1
            if limit and count >= limit:
                break

    def get_ticket(self, record_id):
        # A production adapter should use local Business Object IDs / public-ID
        # lookup operations. This intentionally avoids pretending those IDs are portable.
        raise NotImplementedError("Implement local Cherwell Incident lookup using your Business Object identifiers.")

    def get_asset(self, record_id):
        raise NotImplementedError("Implement local Cherwell asset/CI mapping.")

    def iter_assets(self, *, updated_since=None, limit=None, raw_filter=None):
        raise NotImplementedError("Implement a saved-search-backed asset iterator for the local Cherwell schema.")
