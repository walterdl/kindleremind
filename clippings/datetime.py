from datetime import date
from datetime import datetime
import dateutil.tz as tz
from clippings.months import SPANISH_MONTHS


def get_datetime(text):
    """Abstract the datetime from the metadata of a clipping.

    Args:
        text (str): The metadata of a clipping.
        Example: "- Your Highlight on page 92 | [location 1406-1407 |] Added on Saturday, 26 March 2016 14:59:39"

    Returns:
        datetime: The datetime of the clipping as a datetime object with local timezone.
    """
    return _build_datetime(**_datetime_parts(text))


def _datetime_parts(text):
    parts = text.split('|')

    # Some clipping metadata have two location sections divided by pipe (|).
    # We ask for the last one because it's the one that contains the datetime.
    # Example of result: "Added on Monday, 1 January 2018 00:00:27"
    text = parts[2].strip() if len(parts) > 2 else parts[1].strip()

    [lang_hint, datetime_text] = text.split(',')
    split = _get_datetime_splitter_by_lang(lang_hint)

    return split(datetime_text.strip())


def _get_datetime_splitter_by_lang(lang_hint):
    if lang_hint.startswith("Añadido el"):
        return _split_es_datetime

    return _split_en_datetime


def _split_es_datetime(text):
    # Text example = "17 de diciembre de 2022 3:28:17 p. m."
    parts = text.split(' ')
    time = parts[5].split(':')
    meridiem_indicator = parts[6] if len(parts) > 6 else None

    return {
        "year": parts[4],
        "month_name": parts[2],
        "day": parts[0],
        "hour": time[0],
        "minutes": time[1],
        "seconds": time[2],
        "meridiem_indicator": meridiem_indicator,
    }


def _split_en_datetime(text):
    # Text example = "26 March 2016 2:59:39 p. m."
    parts = text.split(' ')
    time = parts[3].split(':')
    meridiem_indicator = parts[4] if len(parts) > 4 else None

    return {
        "year": parts[2],
        "month_name": parts[1],
        "day": parts[0],
        "hour": time[0],
        "minutes": time[1],
        "seconds": time[2],
        "meridiem_indicator": meridiem_indicator,
    }


def _build_datetime(*, year, month_name, day, hour, minutes, seconds, meridiem_indicator):
    date = _get_date(
        year=year,
        month_name=month_name,
        day=day,
    )
    time = _get_time(
        hour=hour,
        minutes=minutes,
        seconds=seconds,
        meridiem_indicator=meridiem_indicator,
    )

    return datetime.combine(date=date, time=time)


def _get_time(*, hour, minutes, seconds, meridiem_indicator):
    hour = _add_zero_padding(hour)
    minutes = _add_zero_padding(minutes)
    seconds = _add_zero_padding(seconds)
    time = f'{hour}:{minutes}:{seconds}'

    if meridiem_indicator:
        # It's 12 hours format.
        meridiem_designation = 'AM' if 'a' in meridiem_indicator.lower() else 'PM'
        time = f'{time} {meridiem_designation}'
        time_format = '%I:%M:%S %p'
    else:
        time_format = '%H:%M:%S'

    result = datetime.strptime(time, time_format)
    # Adds local timezone.
    result = result.replace(tzinfo=tz.tzlocal())

    return result.timetz()


def _add_zero_padding(x): return x if len(x) == 2 else f"0{x}"


def _get_date(*, day, month_name, year):
    return date(
        year=int(year),
        month=_month_number(month_name),
        day=int(day)
    )


def _month_number(month_name):
    try:
        return datetime.strptime(month_name, '%B').month
    except ValueError:
        # Month name not recognized. Try in Spanish.
        if month_name.lower() in SPANISH_MONTHS:
            return SPANISH_MONTHS.index(month_name.lower()) + 1
        # Month name not recognized in Spanish either. Raise an exception.
        raise
