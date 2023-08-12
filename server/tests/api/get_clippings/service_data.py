import pytest
from unittest.mock import Mock
from datetime import datetime
from kindleremind.api.get_clippings.service import GetClippingsService


@pytest.fixture()
def storage_clippings():
    return [
        {
            'storage_value': {
                'key': 1,
                'timestamp': datetime.fromisoformat('2020-01-01T01:00:00'),
            },
            'iso_timestamp': '2020-01-01T01:00:00'
        },
        {
            'storage_value': {
                'key': 2,
                'timestamp': datetime.fromisoformat('2022-02-21T02:00:00'),
            },
            'iso_timestamp': '2022-02-21T02:00:00'
        }
    ]


@pytest.fixture()
def service(storage_query_result):
    class DummyStorage:
        def query_clippings(self, *args):
            return storage_query_result

    storage = DummyStorage()
    return GetClippingsService(Mock(storage, wraps=storage))


@pytest.fixture()
def storage_query_result(storage_clippings):
    return [x['storage_value'] for x in storage_clippings]
