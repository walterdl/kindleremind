import requests
from .config import config


def send_clippings(clippings):
    response = requests.post(config.server_url, json=clippings, headers={
        'Authorization': config.server_api_key})

    if _is_not_2xx(response):
        raise Exception(_error_message(response))


def _is_not_2xx(response):
    return response.status_code < 200 or response.status_code > 300


def _error_message(response):
    try:
        message = response.json()['message']

        return message
    except Exception:
        return response.text
