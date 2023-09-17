import pytest
from unittest.mock import Mock

from kindleremind.api.post_push_token.service import StorePushTokenService


@pytest.fixture()
def invalid_push_tokens():
    return [
        None,
        True,
        1,
        {},
        '',
        '   '
    ]


@pytest.fixture()
def service():
    return StorePushTokenService(Mock())


def test_throw_if_push_is_invalid(invalid_push_tokens, service):
    for push_token in invalid_push_tokens:
        with pytest.raises(Exception) as exception:
            service.store(push_token)

        assert exception.value.args[0] == 'Invalid push token'


def test_saves_push_token_using_storage(service):
    service.store('The push token')
    service._storage.save_token.assert_called_once_with(
        'The push token')
