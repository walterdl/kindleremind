from enum import Enum
import json


def print_to_file(clippings):
    with open('data/result.json', '+w', encoding='utf-8') as results_file:
        results_file.write(_to_json(clippings))


def _to_json(thing):
    return json.dumps(thing, indent=2, sort_keys=True, default=_custom_encoder)


def _custom_encoder(obj):
    if isinstance(obj, Enum):
        return obj.name
    raise TypeError(
        f"Object of type '{obj.__class__.__name__}' is not JSON serializable")
