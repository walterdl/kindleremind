import json
import pytest
from kindleremind.lib.auth_handler.base import get_handler_wrapper


@pytest.fixture()
def app_context():
    return {
        'email': 'MyEmail'
    }


@pytest.fixture()
def event():
    return {
        'body': 'Hello world'
    }


@pytest.fixture()
def app_context_builder(app_context):
    return lambda _event: app_context


def test_injects_app_context_given_by_app_context_builder(event, app_context, app_context_builder):
    def handler(event, _):
        assert event['app_context'] == app_context

    wrapped_handler = get_handler_wrapper(handler, app_context_builder)
    lambda_context = {}
    wrapped_handler(event, lambda_context)


def test_return_response_as_json_if_given(event, app_context_builder):
    def handler(_, __):
        return {
            'Hello': 'Lambda handler response'
        }

    wrapped_handler = get_handler_wrapper(handler, app_context_builder)
    lambda_context = {}
    response = wrapped_handler(event, lambda_context)

    assert response == {
        'statusCode': 200,
        'body': json.dumps({'Hello': 'Lambda handler response'}),
        'headers': {
            'Content-Type': 'application/json',
        }
    }


def test_return_response_without_body_if_no_result_given(event, app_context_builder):
    def handler(_, __):
        # An operation without any result
        ...

    wrapped_handler = get_handler_wrapper(handler, app_context_builder)
    lambda_context = {}
    response = wrapped_handler(event, lambda_context)

    assert response == {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        }
    }
