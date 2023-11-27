from unittest.mock import Mock
import pytest
import pymongo

from kindleremind.api.get_schedules.storage import Storage
from tests.api.common_fixtures import doc_bid, doc_id, app_context


@pytest.fixture()
def instance(doc_bid, app_context):
    schedules = [
        {
            '_id': doc_bid,
            'user': app_context['email'],
        }
    ]
    collection = Mock()
    collection.find.return_value = schedules

    return Storage(collection)


def test_gets_schedules_of_given_user(instance, app_context):
    instance.get_user_schedules(app_context['email'])

    instance.collection.find.assert_called_once()
    assert instance.collection.find.call_args.args[0] == {
        'user': app_context['email']
    }


def test_gets_schedules_sorted_by_datetime(instance, app_context):
    instance.get_user_schedules(app_context['email'])

    assert instance.collection.find.call_args.kwargs['sort'] == [
        ('datetime', pymongo.DESCENDING)]


def test_formats_results_ids(instance, app_context, doc_id):
    result = instance.get_user_schedules(app_context['email'])
    result = list(result)

    assert result[0]['id'] == doc_id
    assert '_id' not in result[0]
