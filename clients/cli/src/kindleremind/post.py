import requests
from kindleremind.config import config
from .clippings.json import marshall


def send_clippings(clippings):
    response = requests.post(
        config().server_url,
        data=marshall(clippings),
        headers=_headers()
    )

    if _is_not_2xx(response):
        raise Exception(_error_message(response))


def _headers():
    return {
        'Authorization': config().api_key,
        'Content-Type': 'application/json'
    }


def _is_not_2xx(response):
    return response.status_code < 200 or response.status_code > 300


def _error_message(response):
    try:
        message = response.json()['message']
    except Exception:
        message = response.text

    return 'Error posting clippings: {}'.format(message)
