import pytest
from unittest.mock import Mock
from datetime import datetime

from kindleremind.api.post_api_key.storage import ApiKeyStorage
from tests.api.common_fixtures import app_context


@pytest.fixture(scope="module")
def datetime_now():
    return datetime.now()


@pytest.fixture()
def token():
    return 'API Key token value'


@pytest.fixture()
def instance(app_context, token, datetime_now):
    result = ApiKeyStorage(app_context, Mock(), lambda: token)
    result._now = lambda: datetime_now

    return result


def test_saves_api_key_with_current_date(instance, datetime_now):
    instance.save_api_key('API Key input name')

    assert instance.collection.insert_one.call_args.args[0]['createdAt'] == datetime_now


def test_saves_api_key_with_user_context(instance, app_context):
    instance.save_api_key('API Key input name')

    assert instance.collection.insert_one.call_args.args[0]['user'] == app_context['email']


def test_saves_api_key_with_generated_key_value(instance, token):
    instance.save_api_key('API Key input name')

    assert instance.collection.insert_one.call_args.args[0]['value'] == token


def test_saves_api_key_with_given_name(instance):
    input_name = 'API Key input name'

    instance.save_api_key(input_name)

    assert instance.collection.insert_one.call_args.args[0]['name'] == input_name


def test_returns_created_api_key_record(instance, token, app_context, datetime_now):
    input_name = 'API Key input name'

    result = instance.save_api_key(input_name)

    assert result == {
        'name': input_name,
        'value': token,
        'user': app_context['email'],
        'createdAt': datetime_now
    }
