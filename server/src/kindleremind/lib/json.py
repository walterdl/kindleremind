import json


def unmarshall(val, *, return_none_if_error=False, **kwargs):
    try:
        result = json.loads(val)

        if not result and 'default' in kwargs.keys():
            return kwargs['default']

        return result
    except json.JSONDecodeError:
        if return_none_if_error:
            return None
        raise
