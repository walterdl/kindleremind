import json
from .metadata import CLIPPING_TYPE


def marshall(clippings):
    return json.dumps(clippings, indent=2, sort_keys=True, default=_custom_encoder)


def _custom_encoder(obj):
    if isinstance(obj, CLIPPING_TYPE):
        return obj.name
    raise TypeError(
        f"Clipping is not JSON serializable (type '{obj.__class__.__name__}')")
