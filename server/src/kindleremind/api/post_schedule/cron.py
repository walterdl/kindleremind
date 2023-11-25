from datetime import datetime

_WEEKDAY_MAP = {
    '0': 'SUN',
    '1': 'MON',
    '2': 'TUE',
    '3': 'WED',
    '4': 'THU',
    '5': 'FRI',
    '6': 'SAT',
}


def generate_cron_expression(schedule):
    dt = schedule['datetime']

    # E.g. '1', '2', '4' -> 'MON-TUE-THU'
    cron_days = ','.join(_WEEKDAY_MAP[day] for day in schedule['weekdays'])

    cron_expression = f"{dt.minute} {dt.hour} ? * {cron_days} *"

    return cron_expression
