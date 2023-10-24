import json
import pytest
from kindleremind.lib.auth_handler import auth_handler


@pytest.fixture()
def app_context():
    return {
        'email': 'MyEmail'
    }


@pytest.fixture()
def lambda_context():
    return {}


@pytest.fixture()
def event(app_context):
    return {
        'requestContext': {
            'authorizer': {
                'jwt': {
                    'claims': {
                        'email': app_context['email']
                    }
                }
            }
        }
    }


def test_injects_app_context_in_event(event, lambda_context, app_context):
    @auth_handler
    def handler(event, _):
        assert event['app_context'] == app_context

    handler(event, lambda_context)


def test_return_response_as_json_if_given(event, lambda_context):
    @auth_handler
    def handler(_, __):
        return {
            'Hello': 'There'
        }

    response = handler(event, lambda_context)
    assert response == {
        'statusCode': 200,
        'body': json.dumps({'Hello': 'There'}),
        'headers': {
            'Content-Type': 'application/json',
        }
    }


def test_return_response_without_body_if_no_result_given(event, lambda_context):
    @auth_handler
    def handler(_, __):
        # An operation without any result
        ...

    response = handler(event, lambda_context)
    assert response == {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        }
    }
