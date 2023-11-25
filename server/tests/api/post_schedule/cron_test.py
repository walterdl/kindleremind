import pytest
from datetime import datetime

from kindleremind.api.post_schedule.cron import generate_cron_expression


@pytest.mark.parametrize(
    ['input_', 'expected'],
    [
        (
            {
                'datetime': datetime.fromisoformat('2023-11-22T12:00:00.000Z'),
                'weekdays': ['1', '2', '4'],
            },
            '0 12 ? * MON,TUE,THU *'
        ),
        (
            {
                'datetime': datetime.fromisoformat('2023-11-22T12:00:00.000Z'),
                'weekdays': ['0', '1', '2', '3', '4', '5', '6'],
            },
            '0 12 ? * SUN,MON,TUE,WED,THU,FRI,SAT *'
        ),
        (
            {
                'datetime': datetime.fromisoformat('2023-11-22T12:00:00.000Z'),
                'weekdays': ['0'],
            },
            '0 12 ? * SUN *'
        ),
        (
            {
                'datetime': datetime.fromisoformat('2023-11-22T12:00:00.000Z'),
                'weekdays': ['1', '3', '5'],
            },
            '0 12 ? * MON,WED,FRI *'
        ),
        (
            {
                'datetime': datetime.fromisoformat('2023-11-22T12:00:00.000Z'),
                'weekdays': ['0', '2', '4', '6'],
            },
            '0 12 ? * SUN,TUE,THU,SAT *'
        ),
    ]
)
def test_generates_cron_expression_correctly(input_, expected):
    result = generate_cron_expression(input_)

    assert result == expected
