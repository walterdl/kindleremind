import pytest
from unittest.mock import patch
from kindleremind.api.authorizer.handler import lambda_handler


class DummyConfig():
    def __init__(self):
        self.authorizer_token = 'Dummy auth token'


@patch('kindleremind.api.authorizer.handler.config', DummyConfig())
def test_returns_false_if_token_is_not_valid():
    result = lambda_handler({
        'headers': {
            'Authorization': 'A different auth token'
        }
    })

    assert result['isAuthorized'] == False


@patch('kindleremind.api.authorizer.handler.config', new_callable=DummyConfig)
def test_returns_true_if_token_is_not_valid(config):
    result = lambda_handler({
        'headers': {
            'Authorization': config.authorizer_token
        }
    })

    assert result['isAuthorized'] == True
