from unittest.mock import patch
import pytest
import json
import copy
from datetime import datetime

from kindleremind.workers.send_clipping.sender import ClippingSender
from firebase_admin import messaging
from tests.api.common_fixtures import clippings


@pytest.fixture()
def device_token():
    return 'Dummy device token'


@pytest.fixture()
def clipping(clippings):
    result = copy.deepcopy(clippings['formatted'][0])
    return {
        **result,
        'timestamp': datetime.now()
    }


@pytest.fixture()
def test_instance():
    with patch('firebase_admin.messaging.send') as send_mock:
        yield {'sender': ClippingSender(messaging), 'send_mock': send_mock}


def test_send_to_specified_device_token(test_instance, device_token, clipping):
    sender = test_instance['sender']
    sender.send_clipping(clipping, device_token)

    message = test_instance['send_mock'].call_args.args[0]
    assert message.token == device_token


def test_send_given_token_as_data(test_instance, device_token, clipping):
    sender = test_instance['sender']

    sender.send_clipping(clipping, device_token)

    message = test_instance['send_mock'].call_args.args[0]
    assert message.data == {
        'clipping': json.dumps({
            **clipping,
            'timestamp': clipping['timestamp'].isoformat()
        })
    }


def test_send_with_high_priority(test_instance, device_token, clipping):
    sender = test_instance['sender']

    sender.send_clipping(clipping, device_token)

    message = test_instance['send_mock'].call_args.args[0]
    assert isinstance(
        message.android,
        messaging.AndroidConfig
    )
    assert message.android.priority == 'high'
