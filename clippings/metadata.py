from enum import Enum


def get_metadata(text):
    try:
        # Removes initial dash and space
        text = text[2:]
        return {
            "type": _get_type(text),
            "location": _get_location(text),
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
