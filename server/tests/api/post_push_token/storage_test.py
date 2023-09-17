import pytest
from unittest.mock import Mock

from kindleremind.api.post_push_token.storage import Storage


@pytest.fixture()
def instance():
    return Storage(Mock())


@pytest.fixture()
def push_token():
    return 'The push token'


def test_replace_exiting_record(instance, push_token):
    instance.save_token(push_token)
    upsert = instance.collection.find_one_and_replace.call_args.kwargs['upsert']

    assert upsert == True


def test_filter_by_push_token(instance, push_token):
    instance.save_token(push_token)
    used_filter = instance.collection.find_one_and_replace.call_args.args[0]

    assert used_filter == {'token': push_token}


def test_create_new_record_with_same_token(instance, push_token):
    instance.save_token(push_token)
    new_record = instance.collection.find_one_and_replace.call_args.args[1]

    assert new_record == {'token': push_token}
