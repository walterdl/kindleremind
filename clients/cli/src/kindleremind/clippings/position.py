from enum import Enum


def get_position(text):
    """Abstract the position from the metadata of a clipping.

    Args:
        text (str): The metadata of a clipping.
        Example: "- Your Highlight on page 92 | [location 1406-1407 |] Added on Saturday, 26 March 2016 14:59:39"

    Returns:
        dict: The position of the clipping as a dict with the keys "page" and "location" (some clippings don't have pages).
    """
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
