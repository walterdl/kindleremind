from datetime import datetime, timezone


def validate_input(schedule):
    if not schedule or not isinstance(schedule, dict):
        _throw('Empty schedule')

    _validate_datetime(schedule)
    _validate_weekdays(schedule)


def _validate_datetime(schedule):
    if not isinstance(schedule.get('datetime'), str):
        _throw('Invalid datetime')

    try:
        datetime_parsed = datetime.fromisoformat(schedule['datetime'])

        if datetime_parsed.tzinfo != timezone.utc:
            _throw('Datetime is not in UTC')
    except ValueError:
        _throw('Invalid datetime format')


def _validate_weekdays(schedule):
    if not isinstance(schedule.get('weekdays'), list):
        _throw('Invalid weekdays')

    if len(schedule['weekdays']) == 0:
        _throw('Weekdays is empty list')

    for weekday in schedule.get('weekdays'):
        if not isinstance(weekday, str):
            raise _throw('Weekdays contains non-string value')

        if not weekday.isdigit():
            raise _throw('Weekdays contains non-digit')

        if int(weekday) not in range(0, 7):
            raise _throw('Weekdays out of range')


def _throw(msg):
    raise Exception('Invalid schedule: {}'.format(msg))
