import pytest
from unittest.mock import Mock
from datetime import datetime

from kindleremind.api.post_api_key.service import PostApiKeyService
from tests.api.common_fixtures import doc_id


@pytest.fixture()
def api_key(doc_id):
    return {
        'id': doc_id,
        'name': 'The name',
        'value': 'The value',
        'createdAt': datetime.now()
    }


@pytest.fixture()
def instance(api_key):
    storage = Mock()
    storage.save_api_key.return_value = api_key

    return PostApiKeyService(storage)


def test_saves_api_key_using_storage(instance):
    input_name = 'Input API Key name'
    instance.save_api_key(input_name)

    assert instance.storage.save_api_key.call_args.args[0] == input_name


def test_returns_complete_api_key_record(instance, api_key, doc_id):
    input_name = 'Input API Key name'
    result = instance.save_api_key(input_name)

    assert result == {
        'id': doc_id,
        'name': api_key['name'],
        'value': api_key['value'],
        'createdAt': api_key['createdAt'].isoformat()
    }
