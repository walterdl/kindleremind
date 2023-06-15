from enum import Enum
import json


def print(thing):
    with open('data/result.json', '+w', encoding='utf-8') as results_file:
        results_file.write(to_json(thing))


def to_json(thing):
    return json.dumps(thing, indent=2, sort_keys=True, default=custom_encoder)


def custom_encoder(obj):
    if isinstance(obj, Enum):
        return obj.name
    raise TypeError(
        f"Object of type '{obj.__class__.__name__}' is not JSON serializable")
