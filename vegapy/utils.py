import yaml
import logging
import logging.config

import datetime


def timestamp_to_datetime(ts: int, nano: bool = True):
    if nano:
        ts = ts / 1e9
    return datetime.datetime.fromtimestamp(ts)


def datetime_to_timestamp(dt: datetime.datetime, nano: bool = True) -> int:
    ts = dt.timestamp()
    if nano:
        ts = ts * 1e9
    return int(ts)


def padded_int_to_float(padded_int: int, decimals: int) -> float:
    padded_int = int(padded_int) if isinstance(padded_int, str) else padded_int
    return float(padded_int) * 10**-decimals
