import pytest
from unittest.mock import Mock

from kindleremind.workers.send_clipping.service import ClippingSenderService


@pytest.fixture()
def token():
    return {
        'value': 'Token value',
    }


@pytest.fixture()
def clipping():
    return {
        'title': 'Clipping title',
    }


@pytest.fixture()
def service(clipping, token):
    clippings_storage = Mock()
    clippings_storage.get_random_clipping.return_value = clipping

    tokens_storage = Mock()
    tokens_storage.get_token.return_value = token

    sender = Mock()

    return ClippingSenderService(clippings_storage, tokens_storage, sender)


def test_get_token_from_storage(service):
    service.send_clipping()
    service._tokens_storage.get_token.assert_called_once()


def test_cancel_operation_if_no_token_in_storage(service):
    service._tokens_storage.get_token.return_value = None
    service.send_clipping()
    service._clippings_storage.get_random_clipping.assert_not_called()


def test_get_random_clipping_from_storage(service):
    service.send_clipping()
    service._clippings_storage.get_random_clipping.assert_called_once()


def test_cancel_sending_if_no_clipping_in_storage(service, token):
    service._clippings_storage.get_random_clipping.return_value = None
    service.send_clipping()
    service._sender.send_clipping.assert_not_called()


def test_send_clipping_using_sender_service_for_token_proto(service, token, clipping):
    service.send_clipping()
    service._sender.send_clipping.assert_called_once_with({
        'token': token,
        'clipping': clipping
    })
