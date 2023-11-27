from unittest.mock import Mock
from bson.objectid import ObjectId
import pytest

from kindleremind.api.delete_schedule.storage import Storage
from tests.api.common_fixtures import doc_id


@pytest.fixture()
def instance():
    return Storage(collection=Mock())


def test_delete_schedule_of_user_identified_by_given_id(instance, doc_id):
    instance.delete_schedule({
        'user': 'The user identifier',
        'id': doc_id
    })

    instance.collection.delete_one.assert_called_once_with({
        'user': 'The user identifier',
        '_id': ObjectId(doc_id),
    })
