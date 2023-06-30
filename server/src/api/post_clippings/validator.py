def validate_clippings(clippings):
    """Validate the structure of each clipping

    Throws ValueError if any clipping is invalid.
    """
    _check_collection(clippings)
    for clipping in clippings:
        _check_clipping(clipping)
        _check_fields(clipping)


def _check_collection(clippings):
    if not isinstance(clippings, list):
        raise ValueError(
            f"Expected a list of clippings, got {type(clippings)}")


def _check_clipping(clipping):
    if not isinstance(clipping, dict):
        raise ValueError(
            f"Expected a dict, got {type(clipping)}")


def _check_fields(clipping):
    """Check that all clipping fields are present and have the correct type.

    Throws ValueError if any field is invalid.
    """

    _check_required_str_fields(clipping)
    _check_content(clipping)
    _check_position(clipping)


def _check_required_str_fields(clipping):
    required_str_fields = ('author', 'timestamp', 'title', 'type')
    for field in required_str_fields:
        if _empty_str(field, clipping):
            raise ValueError(f"Missing required field: {field}")


def _empty_str(field, clipping):
    return (
        field not in clipping or
        not isinstance(clipping[field], str) or
        not len(clipping[field])
    )


def _check_content(clipping):
    if 'content' not in clipping:
        raise ValueError('Missing required field: content')

    if not isinstance(clipping['content'], str) and clipping['content'] == None:
        raise ValueError('Invalid content field')


def _check_position(clipping):
    if 'position' not in clipping:
        raise ValueError("Missing required field: position")

    if not isinstance(clipping['position'], dict):
        raise ValueError("Invalid position field")

    if 'location' not in clipping['position']:
        raise ValueError("Missing required field: position.location")

    if _empty_str('location', clipping['position']):
        raise ValueError("Invalid position.location field")

    if "page" in clipping['position'] and _empty_str('page', clipping['position']):
        raise ValueError("Invalid position.page field")
