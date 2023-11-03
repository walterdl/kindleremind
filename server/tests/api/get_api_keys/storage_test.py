import pytest
from unittest.mock import Mock
from datetime import datetime
import pymongo

from kindleremind.api.get_api_keys.storage import Storage
from tests.api.common_fixtures import app_context


@pytest.fixture()
def api_keys():
    return [
        {
            'name': 'Api Key 1',
            'value': 'value-1',
            'createdAt': datetime.fromisoformat('2023-11-04T09:00:00Z')
        },
        {
            'name': 'Api Key 2',
            'value': 'value-2',
            'createdAt': datetime.fromisoformat('2023-11-07T10:00:00Z')
        }
    ]


@pytest.fixture()
def instance(app_context, api_keys):
    api_keys_collection = Mock()
    api_keys_collection.find.return_value = api_keys

    return Storage(app_context, api_keys_collection)


def test_get_api_keys_using_user_context(instance, app_context, api_keys):
    instance.get_api_keys()
    query_filter = instance.api_keys_collection.find.mock_calls[0].args[0]

    assert query_filter == {'user': app_context['email']}


def test_get_api_keys_sorted_by_creation_date(instance):
    instance.get_api_keys()
    query_sorting = instance.api_keys_collection.find.mock_calls[0].kwargs['sort']

    assert query_sorting == [('createdAt', pymongo.DESCENDING)]


def test_does_not_include_native_id(instance):
    instance.get_api_keys()
    query_projection = instance.api_keys_collection.find.mock_calls[0].kwargs['projection']

    assert query_projection == {'_id': False}
