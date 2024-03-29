import pytest
from unittest.mock import patch, Mock
from requests.exceptions import JSONDecodeError
from kindleremind.post import send_clippings
from kindleremind.clippings.json import marshall


@pytest.fixture()
def config():
    dummy_config = Mock(
        server_url='http://example.com',
        api_key='Dummy api key'
    )

    with patch('kindleremind.post.config', lambda: dummy_config):
        yield dummy_config


@pytest.fixture()
def requests():
    request_mock = Mock()
    request_mock.post.return_value = Mock(status_code=200)
    with patch('kindleremind.post.requests', request_mock):
        yield request_mock


@pytest.fixture()
def clippings():
    return [
        {
            "author": "Ray Bradbury",
            "content": None,
            "position": {
                "location": "346"
            },
            "timestamp": "2016-03-26T15:46:21-05:00",
            "title": "Fahrenheit 451",
            "type": "BOOKMARK"
        }
    ]


def test_sends_to_the_server_url(config, requests, clippings):
    send_clippings(clippings)
    url = requests.mock_calls[0].args[0]

    assert url == config.server_url


def test_sends_clippings_as_json_encoded(requests, clippings):
    send_clippings(clippings)
    json_data = requests.mock_calls[0].kwargs['data']
    assert json_data == marshall(clippings)


def test_sends_json_content_type_header(requests, clippings):
    send_clippings(clippings)
    headers = requests.mock_calls[0].kwargs['headers']

    assert headers['Content-Type'] == 'application/json'


def test_sends_the_authorization_token(config, requests, clippings):
    send_clippings(clippings)
    headers = requests.mock_calls[0].kwargs['headers']

    assert headers['Authorization'] == config.api_key


def test_throws_if_status_code_is_not_2xx(requests, clippings):
    status_codes = [100, 301, 400, 500]
    for code in status_codes:
        requests.post.return_value = Mock(status_code=code)
        with pytest.raises(Exception):
            send_clippings(clippings)


def test_throws_exception_with_server_message_if_there_is_any(requests, clippings):
    def json_response(): return {'message': 'Dummy error message'}
    requests.post.return_value = Mock(status_code=500, json=json_response)
    with pytest.raises(Exception) as exception:
        send_clippings(clippings)

    assert str(exception.value) == 'Error posting clippings: Dummy error message'


def test_throws_exception_with_response_text_if_there_is_no_server_message(clippings, requests):
    def json_response(): raise JSONDecodeError('Incorrect json response', '', 0)
    response_text = 'Textual error representation'
    requests.post.return_value = Mock(
        status_code=500, text=response_text, json=json_response)

    with pytest.raises(Exception) as exception:
        send_clippings(clippings)

    assert str(exception.value) == 'Error posting clippings: {}'.format(
        response_text)
