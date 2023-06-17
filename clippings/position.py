from enum import Enum


def get_position(text):
    parts = text.split('|')

    result = {
        _get_type(parts[0]): _get_number(parts[0])
    }

    if len(parts) > 2:
        result[_get_type(parts[1])] = _get_number(parts[1])

    return result


def _get_number(text):
    # I assume the number is the last word
    return text.strip().split(' ').pop()


class LOCATION_TYPE(Enum):
    PAGE = 1
    POSITION = 2


_POSITIONS = [
    {
        'type': 'page',
        "texts": ('page', 'página')
    },
    {
        'type': "location",
        'texts': ("location", "posición")
    },
]


def _get_type(text):
    for position in _POSITIONS:
        for position_text in position['texts']:
            if position_text in text.lower():
                return position['type']
    raise ValueError("Position type not found")
