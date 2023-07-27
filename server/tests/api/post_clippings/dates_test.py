from datetime import datetime
from api.post_clippings.dates import iso_to_utc_datetime


def test_iso_to_utc_datetime_with_tz():
    result = iso_to_utc_datetime('2022-12-17T14:30:30-05:00')

    assert isinstance(result, datetime)
    assert result.isoformat() == '2022-12-17T19:30:30+00:00'


def test_iso_to_utc_datetime_without_tz():
    result = iso_to_utc_datetime('2022-12-17T19:30:30+00:00')

    assert isinstance(result, datetime)
    assert result.isoformat() == '2022-12-17T19:30:30+00:00'
