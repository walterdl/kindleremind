from enum import Enum
from datetime import datetime
import dateutil.tz as tz
from clippings.months import SPANISH_MONTHS


def get_metadata(text):
    try:
        # Removes initial dash and space
        text = text[2:]
        return {
            "type": _get_type(text),
            "location": _get_location(text),
            "timestamp": _get_timestamp(text),
        }
    except IndexError:
        raise ValueError("Malformed clipping metadata")


_BOOKMARK_TEXT = ("Your Bookmark", "El marcador")
_HIGHLIGHT_TEXT = ("Your Highlight", "La subrayado")


class CLIPPING_TYPE(Enum):
    BOOKMARK = 1
    HIGHLIGHT = 2


def _get_type(text):
    if text.startswith(_BOOKMARK_TEXT):
        return CLIPPING_TYPE.BOOKMARK
    elif text.startswith(_HIGHLIGHT_TEXT):
        return CLIPPING_TYPE.HIGHLIGHT
    else:
        raise ValueError("Unknown clipping type")


class LOCATION_TYPE(Enum):
    PAGE = 1
    POSITION = 2


_LOCATIONS = [
    {
        "type": LOCATION_TYPE.PAGE,
        "texts": ("on page", "en la página")
    },
    {
        "type": LOCATION_TYPE.POSITION,
        "texts": ("at location", "en la posición")
    },
]


def _get_location(text):
    for location in _LOCATIONS:
        location_number = _search_location_number(text, location["texts"])
        if location_number:
            return {
                "type": location["type"],
                "value": location_number,
            }
    else:
        raise ValueError("Unknown location type")


def _search_location_number(text, location_texts):
    for location_text in location_texts:
        if location_text in text:
            location_index = text.index(location_text)
            # Removes the location text closer to the location number
            # It adds +1 to skip the space.
            # Example: "on page 17 | rest of text..." -> "17 | rest of text..."
            text = text[location_index + len(location_text) + 1:]
            end_of_position_number = text.find(" ")

            return text[:end_of_position_number]


def _get_timestamp(text):
    # 1. Import datetime module
    # 2. Get the OS timezone using dateutil.tz.tzlocal()
    # 3. Remove any token from the text to leave only numbers that can represent a timestamp.
    #    You will have to identify both English and Spanish tokens.
    #    Set the result in a dictionary whose keys represent the datetime tokens.
    #    Example: "Added on Monday, 1 January 2018 00:00:00" -> {"day": 1, "month": 1, "year": 2018, "hour": 0, "minute": 0, "second": 0}
    # 4. Use datetime.datetime() to create a datetime object using the dictionary created in the previous step.
    # 5. Set the OS timezone to the datetime object using datetime.replace()
    # 6. Return the datetime ISO format using datetime.isoformat()
    datetime_parts = _get_datetime_parts(text)
    print("to get timestamp", tz.tzlocal())

    return datetime(
        datetime_parts['year'],
        datetime_parts['month'],
        datetime_parts['day'],
        datetime_parts['hour'],
        datetime_parts['minute'],
        datetime_parts['second'],
        tzinfo=tz.tzlocal()  # Local timezone
    ).isoformat()


def _get_datetime_parts(text):
    """
    Returns a dictionary with the datetime parts given the metadata text of a clipping.
    Example:
        - Input: "- Your Bookmark at location 346 | Added on Monday, 1 January 2018 00:00:27"
        - Output: {"day": 1, "month": 1, "year": 2018, "hour": 0, "minute": 0, "second": 27}
    """
    # Gets the datetime part of the text.
    # Example of result: "Added on Monday, 1 January 2018 00:00:27"
    text = text.split('|')[1].strip()

    # Removes the day name from the text.
    # Example of result: "1 January 2018 00:00:27"
    text = text.split(',')[1].strip()

    datetime = text.split(' ')
    _month_number(datetime[1])
    time = datetime[3].split(':')

    return {
        "day": int(datetime[0]),
        "month": _month_number(datetime[1]),
        "year": int(datetime[2]),
        "hour": int(time[0]),
        "minute": int(time[1]),
        "second": int(time[2]),
    }


def _month_number(month_name):
    try:
        return datetime.strptime(month_name, '%B').month
    except ValueError:
        # Month name not recognized. Try in Spanish.
        if month_name.lower() in SPANISH_MONTHS:
            return SPANISH_MONTHS.index(month_name.lower()) + 1
        # Month name not recognized in Spanish either. Raise an exception.
        raise
