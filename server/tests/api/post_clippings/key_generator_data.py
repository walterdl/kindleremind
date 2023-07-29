import pytest
from unittest.mock import Mock
from api.post_clippings.key_generator import ClippingKeyGenerator
from tests.api.common_fixtures import clippings


@pytest.fixture()
def key_generator():
    return ClippingKeyGenerator(Mock(return_value="A dummy key"))


@pytest.fixture()
def clippings_without_content(clippings):
    base_clipping = clippings['base'][0]
    return [
        {
            **base_clipping,
            'content': None,
            'position': {'location': '123'}
        },
        {
            **base_clipping,
            'content': '',
            'position': {'location': '123'}
        },
    ]


@pytest.fixture()
def no_content_but_location_and_page(clippings):
    return {
        **clippings['base'][0],
        'content': None,
        'position': {'location': '123', 'page': '456'}
    }
