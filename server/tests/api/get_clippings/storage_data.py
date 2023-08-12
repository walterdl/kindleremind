from unittest.mock import Mock
from kindleremind.api.get_clippings.storage import Storage

clippings_list = [
    {'key': 1},
    {'key': 2}
]


def get_storage_instance():
    class DummyClippingsCollection():
        def find(self, _filter, **kwargs):
            return (x for x in clippings_list)

    collection = DummyClippingsCollection()
    spiedCollection = Mock(collection, wraps=collection)

    return Storage(spiedCollection)
