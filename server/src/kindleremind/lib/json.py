import json


def unmarshall(val, *, return_none_if_error=False):
    try:
        result = json.loads(val)
        return result
    except json.JSONDecodeError:
        if return_none_if_error:
            return None
        raise
