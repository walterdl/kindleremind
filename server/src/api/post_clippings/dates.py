from datetime import datetime, timezone


def iso_to_utc_datetime(iso_timestamp):
    """Converts the clipping ISO timestamp to a datetime object with TZ.

    Returns a clipping
    """
    return datetime.fromisoformat(iso_timestamp).astimezone(timezone.utc)
