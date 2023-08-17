import requests
from .config import config
from .clippings.json import marshall


def send_clippings(clippings):
    response = requests.post(
        config.server_url,
        data=marshall(clippings),
        headers=_headers()
    )

    if _is_not_2xx(response):
        raise Exception(_error_message(response))


def _headers():
    return {
        'Authorization': config.server_api_key,
        'Content-Type': 'application/json'
    }


def _is_not_2xx(response):
    return response.status_code < 200 or response.status_code > 300


def _error_message(response):
    try:
        message = response.json()['message']

        return message
    except Exception:
        return response.text
