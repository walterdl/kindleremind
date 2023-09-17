import pytest
from unittest.mock import Mock

from kindleremind.api.delete_push_token.storage import Storage


@pytest.fixture()
def storage():
    return Storage(Mock())


@pytest.fixture()
def push_token():
    return 'The push token'


def test_delete_the_given_token(storage, push_token):
    storage.delete_push_token(push_token)
    storage._collection.delete_one.assert_called_once_with(
        {'token': push_token})
