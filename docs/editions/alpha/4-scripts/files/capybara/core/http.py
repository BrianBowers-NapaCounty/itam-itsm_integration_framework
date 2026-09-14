"""Small HTTP helpers shared by REST connectors."""

from __future__ import annotations
import time
import random


def request_with_retry(session, method, url, *, attempts=4, retry_statuses=(429, 500, 502, 503, 504), **kwargs):
    """Issue an HTTP request with bounded exponential backoff and jitter.

    Authentication/authorization failures (401/403) are deliberately not
    retried here because they normally require credential or permission repair.
    """
    last = None
    for n in range(attempts):
        response = session.request(method, url, timeout=kwargs.pop("timeout", 45), **kwargs)
        last = response
        if response.status_code not in retry_statuses:
            response.raise_for_status()
            return response
        if n < attempts - 1:
            retry_after = response.headers.get("Retry-After")
            if retry_after and str(retry_after).isdigit():
                delay = float(retry_after)
            else:
                delay = min(20.0, (2 ** n) + random.uniform(0.2, 1.2))
            time.sleep(delay)
    last.raise_for_status()
    return last
