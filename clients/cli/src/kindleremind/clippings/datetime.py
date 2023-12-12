from datetime import date
from datetime import datetime
import dateutil.tz as tz
from kindleremind.clippings.months import SPANISH_MONTHS


def get_datetime(metadata):
    """Abstract the datetime from the metadata of a clipping.

    Args:
        text (str): The metadata of a clipping.
        Example: "- Your Highlight on page 92 | [location 1406-1407 |] Added on Saturday, 26 March 2016 14:59:39"

    Returns:
        datetime: The datetime of the clipping as a datetime object with local timezone.
    """
    return _build_datetime(**_datetime_parts(metadata))


def _datetime_parts(metadata):
    datetime_literal_section = _get_datetime_section(metadata)

    lang_hint, *datetime_parts = datetime_literal_section.split(',')
    split = _get_datetime_splitter_by_lang(lang_hint)

    return split([part.strip() for part in datetime_parts])


def _get_datetime_section(metadata):
    """Given a clipping metadata, return the raw datetime text.

    Example input: "- Your Highlight on page 92 | [location 1406-1407 |] Added on Saturday, 26 March 2016 14:59:39"
    Example output: "Added on Saturday, 26 March 2016 14:59:39"
    """
    parts = metadata.split('|')

    # Some clipping metadata have two location sections divided by pipe (|).
    # We ask for the last one because it's the one that contains the datetime.
    # Example of result: "Added on Monday, 1 January 2018 00:00:27"
    return parts[2].strip() if len(parts) > 2 else parts[1].strip()


def _get_datetime_splitter_by_lang(lang_hint):
    if lang_hint.startswith("Añadido el"):
        return _split_es_datetime

    return _split_en_datetime


def _split_es_datetime(datetime_parts):
    # Input example = ["17 de diciembre de 2022 3:28:17 p. m."]
    parts = datetime_parts[0].split(' ')
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


def _split_en_datetime(datetime_parts):
    """
    Input examples:
    Variant 1 = ["26 March 2016 2:59:39 p. m."]

    (Some kindle devices split the month and day before time and use meridiem indicator in uppercase)
    Variant 2 = ["December 01", "2023 9:02:48 PM"]
    """

    if len(datetime_parts) == 2:
        datetime_parts = _normalize_english_variant_2(datetime_parts)

    raw_datetime = datetime_parts[0]
    parts = raw_datetime.split(' ')
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


def _normalize_english_variant_2(datetime_parts):
    # ["December 01", "2023 9:02:48 PM"] -> ["01 December 2016 9:02:48 p. m."]
    month, day = datetime_parts[0].split(' ')
    time_part = datetime_parts[1]
    result = f"{day} {month} {time_part}"

    # Format meridiem indicator to lowercase.
    meridiem_indicator = result.split(' ')[-1:][0]
    meridiem_formats = {
        "PM": "p. m.",
        "AM": "a. m.",
    }
    if meridiem_indicator in meridiem_formats:
        result = result.replace(
            meridiem_indicator, meridiem_formats[meridiem_indicator])

    return [result]


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
