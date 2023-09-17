import pytest
from unittest.mock import Mock

from kindleremind.api.delete_push_token.service import DeletePushTokenService


@pytest.fixture()
def service():
    return DeletePushTokenService(Mock())


@pytest.fixture()
def push_token():
    return 'The push token'


def test_delete_given_token_using_storage(service, push_token):
    service.delete_push_token(push_token)
    service._storage.delete_push_token.assert_called_once_with(push_token)


def test_throws_if_push_token_is_invalid(service):
    invalid_tokens = [
        None,
        '',
        ' ',
        {}
    ]

    for invalid_token in invalid_tokens:
        with pytest.raises(Exception) as excinfo:
            service.delete_push_token(invalid_token)

        assert 'Invalid push token' == str(excinfo.value)
