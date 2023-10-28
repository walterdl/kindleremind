import pytest
from unittest.mock import Mock

from kindleremind.api.get_clippings.storage import Storage
from tests.api.common_fixtures import app_context

clippings_list = [
    {'key': 1},
    {'key': 2}
]


@pytest.fixture()
def instance(app_context):
    class DummyClippingsCollection():
        def find(self, _filter, **kwargs):
            return (x for x in clippings_list)

    collection = DummyClippingsCollection()
    spiedCollection = Mock(collection, wraps=collection)

    return Storage(app_context, spiedCollection)
