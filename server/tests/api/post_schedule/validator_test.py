import pytest
from kindleremind.api.post_schedule.validator import validate_input


@pytest.mark.parametrize(['schedule', 'message'], [
    (None, 'Empty schedule'),
    (dict(), 'Empty schedule'),
    (
        {
            'datetime': 89,
            'weekdays': ['0', '1', '2'],
        },
        'Invalid datetime'
    ),
    (
        {
            'datetime': 'Not a valid ISO 8601',
            'weekdays': ['0', '1', '2'],
        },
        'Invalid datetime format'
    ),
    (
        {
            'datetime': '2020-01-01T00:00:00-05:00',
            'weekdays': ['1', '2'],
        },
        'Datetime is not in UTC'
    ),
    (
        {
            'datetime': '2020-01',
            'weekdays': ['1', '2'],
        },
        'Invalid datetime format'
    ),
    (
        {
            'datetime': '2020-01-01T00:00:00Z',
            'weekdays': None,
        },
        'Invalid weekdays'
    ),
    (
        {
            'datetime': '2020-01-01T00:00:00Z',
            'weekdays': '',
        },
        'Invalid weekdays'
    ),
    (
        {
            'datetime': '2020-01-01T00:00:00Z',
            'weekdays': [],
        },
        'Weekdays is empty list'
    ),
    (
        {
            'datetime': '2020-01-01T00:00:00Z',
            'weekdays': ['1', 2],
        },
        'Weekdays contains non-string value'
    ),
    (
        {
            'datetime': '2020-01-01T00:00:00Z',
            'weekdays': ['1', False],
        },
        'Weekdays contains non-string value'
    ),
    (
        {
            'datetime': '2020-01-01T00:00:00Z',
            'weekdays': ['1s',],
        },
        'Weekdays contains non-digit'
    ),
    (
        {
            'datetime': '2020-01-01T00:00:00Z',
            'weekdays': ['7'],
        },
        'Weekdays out of range'
    ),
])
def test_post_throws_for_invalid_schedule(schedule, message):
    with pytest.raises(Exception) as exception:
        validate_input(schedule)

    assert exception.value.args[0].rfind(message) != -1
