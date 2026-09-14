"""Alert selection plus console/SMTP notifiers."""

from __future__ import annotations
from dataclasses import asdict
from datetime import datetime, timezone
from email.message import EmailMessage
import os, smtplib


def missing_assets(assets):
    words = {"missing","lost","stolen","unable to locate","not found"}
    return [a for a in assets if any(w in str(a.status).lower() for w in words)]


def stale_unassigned_tickets(tickets, *, hours=8):
    now = datetime.now(timezone.utc)
    out = []
    for t in tickets:
        if t.assignee:
            continue
        stamp = t.updated_at or t.opened_at
        if stamp and (now - stamp.astimezone(timezone.utc)).total_seconds() >= hours*3600:
            out.append(t)
    return out


def parts_hold_tickets(tickets, *, days=5):
    now = datetime.now(timezone.utc)
    markers = ("parts","equipment","procure","order","vendor","awaiting")
    out = []
    for t in tickets:
        hold = f"{t.status} {t.hold_reason}".lower()
        stamp = t.updated_at or t.opened_at
        if any(m in hold for m in markers) and stamp and (now-stamp.astimezone(timezone.utc)).days >= days:
            out.append(t)
    return out


class ConsoleNotifier:
    def send(self, subject, text, recipients=None, html=None):
        print("="*72)
        print(subject)
        if recipients:
            print("Recipients:", ", ".join(recipients))
        print(text)
        return True


class SMTPNotifier:
    def __init__(self, cfg):
        s = cfg.section("smtp")
        self.host = s["host"]; self.port = int(s.get("port",587))
        self.starttls = bool(s.get("starttls",True))
        self.username = cfg.env_value("smtp.username_env")
        self.password = cfg.env_value("smtp.password_env")
        self.from_address = s["from_address"]
        self.default_recipients = list(s.get("default_recipients",[]))

    def send(self, subject, text, recipients=None, html=None):
        recipients = list(recipients or self.default_recipients)
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = self.from_address
        msg["To"] = ", ".join(recipients)
        msg.set_content(text)
        if html:
            msg.add_alternative(html, subtype="html")
        with smtplib.SMTP(self.host,self.port,timeout=30) as smtp:
            if self.starttls:
                smtp.starttls()
            if self.username:
                smtp.login(self.username,self.password or "")
            smtp.send_message(msg)
        return True
