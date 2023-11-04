import pytest
from unittest.mock import Mock
from bson.objectid import ObjectId

from kindleremind.api.delete_api_key.storage import ApiKeyStorage
from tests.api.common_fixtures import app_context, doc_id


@pytest.fixture()
def instance(app_context):
    return ApiKeyStorage(app_context, Mock())


def test_delete_api_key_by_given_key(instance, api_key_id):
    instance.delete_api_key(api_key_id)

    assert instance.collection.delete_one.call_args.args[0]['_id'] == ObjectId(
        api_key_id)


def test_delete_api_key_using_user_context(instance, app_context, api_key_id):
    instance.delete_api_key(api_key_id)

    assert instance.collection.delete_one.call_args.args[0]['user'] == app_context['email']
