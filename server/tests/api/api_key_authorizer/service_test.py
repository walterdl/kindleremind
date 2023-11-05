import pytest
from unittest.mock import Mock

from kindleremind.api.api_key_authorizer.service import ApiKeyAuthorizer


@pytest.fixture()
def api_key():
    return {
        'id': 'The API Key ID'
    }


@pytest.fixture()
def instance(api_key):
    storage = Mock()
    storage.get_api_keys.return_value = [api_key]

    return ApiKeyAuthorizer(storage)


def test_gets_api_key_by_token_value(instance):
    api_key_value = 'The API Key value'
    instance.check_api_key(api_key_value)
    docs_filter = instance.storage.get_api_keys.mock_calls[0].args[0]

    assert docs_filter == {'value': api_key_value}


def test_bypasses_user_filter(instance):
    api_key_value = 'The API Key value'
    instance.check_api_key(api_key_value)
    kwargs = instance.storage.get_api_keys.mock_calls[0].kwargs

    assert kwargs['bypass_user_filter'] == True


def test_returns_the_api_key_if_exists(instance, api_key):
    result = instance.check_api_key('The API Key value')

    assert result == api_key


def test_returns_none_if_api_key_does_not_exists(instance):
    instance.storage.get_api_keys.return_value = []
    result = instance.check_api_key('The API Key value')

    assert result == None
