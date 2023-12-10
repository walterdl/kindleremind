from datetime import datetime
import pytest
from unittest.mock import Mock

from kindleremind.api.post_push_token.storage import Storage


@pytest.fixture()
def app_context():
    return {
        'email': 'The user email'
    }


@pytest.fixture()
def instance(app_context):
    return Storage(app_context, Mock())


@pytest.fixture()
def push_token():
    return 'The push token'


def test_replace_exiting_record(instance, push_token):
    instance.save_token(push_token)
    upsert = instance.collection.find_one_and_replace.call_args.kwargs['upsert']

    assert upsert == True


def test_filter_by_user_email(instance, push_token, app_context):
    instance.save_token(push_token)
    used_filter = instance.collection.find_one_and_replace.call_args.args[0]

    assert used_filter == {'user': app_context['email']}


def test_create_new_record_with_same_token(instance, push_token, app_context):
    instance.save_token(push_token)
    new_record = instance.collection.find_one_and_replace.call_args.args[1]

    assert new_record['token'] == push_token
    assert new_record['user'] == app_context['email']
    assert isinstance(new_record['createdAt'], datetime)
