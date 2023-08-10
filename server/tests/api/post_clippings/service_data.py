import pytest
from unittest.mock import Mock
from kindleremind.api.post_clippings.service import WriteClippingsService


_base_clipping = {
    "author": "Martin Fowler",
    "content": "Brevity is the soul of wit,",
    "position": {
        "location": "1181-1181",
        "page": "83"
    },
    "timestamp": "2022-12-17T14:30:30-05:00",
    "title": "Refactoring: Improving the Design of Existing Code, Second Edition (Garner McCloud's Library)",
    "type": "HIGHLIGHT"
}


@pytest.fixture()
def valid_clipping():
    return _base_clipping.copy()


_invalid_positions_values = [True, (), [], 123]
_invalid_positions = [[{**_base_clipping, "position": x}]
                      for x in _invalid_positions_values]

_invalid_content_values = [True, (), [], 123]
_invalid_contents = [[{**_base_clipping, "content": x}]
                     for x in _invalid_content_values]


@pytest.fixture()
def invalid_inputs():
    invalid_values = (None, "", 123, [], True)
    fields = (
        'author',
        'position',
        'timestamp',
        'title',
        'type',
    )
    # Pre-populate with invalid clippings.
    result = []
    result = [None, 123, True, ""]

    for val in invalid_values:
        for field in fields:
            result.append([
                {
                    # Just grab the first valid input.
                    **_base_clipping,
                    field: val
                }
            ])
    result.extend(_invalid_positions)
    result.extend(_invalid_contents)

    return result


@pytest.fixture()
def invalid_collections():
    return (
        None,
        {},
        123,
        True,
        ""
    )


def get_write_clippings_service():
    class DummyKeyGenerator:
        def generate_key(self, _):
            return 'A dummy key'

    return WriteClippingsService(DummyKeyGenerator(), storage=Mock())
