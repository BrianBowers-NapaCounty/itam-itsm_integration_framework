"""Calendar-aligned and rolling reporting windows."""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from calendar import monthrange
from zoneinfo import ZoneInfo


@dataclass(frozen=True, slots=True)
class TimeWindow:
    code: str
    label: str
    start: datetime
    end: datetime

    def contains(self, value: datetime | None) -> bool:
        if value is None:
            return False
        if value.tzinfo is None:
            value = value.replace(tzinfo=timezone.utc)
        return self.start <= value.astimezone(self.start.tzinfo) < self.end


def _tz(name):
    return ZoneInfo(name or "UTC")


def _local_now(tz_name, now=None):
    tz = _tz(tz_name)
    if now is None:
        return datetime.now(tz)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    return now.astimezone(tz)


def _midnight(dt):
    return dt.replace(hour=0, minute=0, second=0, microsecond=0)


def _month_start(dt):
    return dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)


def _shift_months(dt, months):
    n = dt.year * 12 + (dt.month - 1) + months
    year, month0 = divmod(n, 12)
    month = month0 + 1
    day = min(dt.day, monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)


def _quarter_start(dt):
    month = ((dt.month - 1)//3)*3 + 1
    return dt.replace(month=month, day=1, hour=0, minute=0, second=0, microsecond=0)


def named_window(code, *, tz_name="UTC", now=None):
    now = _local_now(tz_name, now)
    today = _midnight(now)
    tomorrow = today + timedelta(days=1)
    week_start = today - timedelta(days=today.weekday())
    month_start = _month_start(today)
    quarter_start = _quarter_start(today)
    year_start = today.replace(month=1, day=1)

    c = code.strip().lower().replace("_","-")
    rolling = {
        "365d":365, "1y":365, "1-year":365,
        "180d":180, "6m":180, "6-month":180,
        "90d":90, "3m":90, "3-month":90,
        "30d":30, "14d":14, "7d":7, "last-week-rolling":7,
    }
    if c in rolling:
        days = rolling[c]
        return TimeWindow(c, f"Last {days} days", now-timedelta(days=days), now)

    if c == "yesterday":
        return TimeWindow(c,"Yesterday",today-timedelta(days=1),today)
    if c in {"wtd","week-to-date","this-week"}:
        return TimeWindow("wtd","Week to date",week_start,now)
    if c == "previous-week":
        return TimeWindow(c,"Previous week",week_start-timedelta(days=7),week_start)
    if c in {"mtd","month-to-date","this-month"}:
        return TimeWindow("mtd","Month to date",month_start,now)
    if c == "previous-month":
        prev = _shift_months(month_start,-1)
        return TimeWindow(c,"Previous month",prev,month_start)
    if c in {"qtd","quarter-to-date","this-quarter"}:
        return TimeWindow("qtd","Quarter to date",quarter_start,now)
    if c == "previous-quarter":
        prev = _shift_months(quarter_start,-3)
        return TimeWindow(c,"Previous quarter",prev,quarter_start)
    if c in {"ytd","year-to-date","this-year"}:
        return TimeWindow("ytd","Year to date",year_start,now)
    if c == "previous-year":
        prev = year_start.replace(year=year_start.year-1)
        return TimeWindow(c,"Previous year",prev,year_start)
    raise KeyError(f"Unknown window: {code}")


def common_windows(*, tz_name="UTC", now=None):
    codes = [
        "1-year","6-month","3-month","30d","14d","7d",
        "yesterday","wtd","previous-week","mtd","previous-month",
        "qtd","previous-quarter","ytd","previous-year",
    ]
    return [named_window(c,tz_name=tz_name,now=now) for c in codes]


def custom_window(start, end, *, label="Custom", code="custom", tz_name="UTC"):
    tz = _tz(tz_name)
    if start.tzinfo is None: start = start.replace(tzinfo=tz)
    if end.tzinfo is None: end = end.replace(tzinfo=tz)
    return TimeWindow(code,label,start,end)
