import pytest
from unittest.mock import patch
from kindleremind.api.authorizer.handler import lambda_handler


@pytest.fixture(autouse=True)
def dummy_token():
    token = 'Dummy auth token'
    with patch('kindleremind.api.authorizer.handler.get_config', lambda _: token):
        yield token


def test_returns_false_if_token_is_not_valid():
    result = lambda_handler({
        'headers': {
            'authorization': 'A different auth token'
        }
    })

    assert result['isAuthorized'] == False


def test_returns_true_if_token_is_not_valid(dummy_token):
    result = lambda_handler({
        'headers': {
            'authorization': dummy_token
        }
    })

    assert result['isAuthorized'] == True
