from enum import Enum
from clippings.datetime import get_datetime
from clippings.position import get_position


def get_metadata(text):
    try:
        # Removes initial dash and space
        text = text[2:]
        return {
            "type": _get_type(text),
            "position": get_position(text),
            "timestamp": get_datetime(text).isoformat(),
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
