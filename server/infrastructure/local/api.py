"""Local API Gateway for testing Lambda functions locally."""

from importlib import import_module
from flask import Flask, request
from endpoints import endpoints
import traceback
import json


app = Flask(__name__)

for path in endpoints:
    for method in endpoints[path].keys():

        @app.route(path, methods=[method.upper()], endpoint=f"{path}_{method}")
        def handler(path=path):
            endpoint_config = endpoints[path][request.method.lower()]
            handler_module = import_module(endpoint_config['handler_module'])
            handler_func = getattr(
                handler_module, endpoint_config['handler_func'])

            try:
                response = handler_func(build_event())

                return format_lambda_response(response, endpoint_config)
            except Exception as error:
                body = {
                    'error': str(error),
                    'traceback': traceback.format_exception(error)
                }

                return body, 500, {'Content-Type': 'application/json'}


def build_event():
    result = {
        'version': '2.0',
        'routeKey': f"{request.method} {request.path}",
        'rawPath': request.path,
        'rawQueryString': request.query_string.decode('utf-8'),
        'cookies': request.cookies,
        'headers': dict(request.headers),
        'queryStringParameters': request.args.to_dict(),
        'requestContext': {
            'http': {
                'method': request.method,
                'path': request.path,
            }
        },
        'body': request.data.decode('utf-8'),
        'isBase64Encoded': False
    }

    with open('./event.json') as context_file:
        context = json.load(context_file)
        # Merge context and base
        result.update(context)

    return result


def format_lambda_response(response, endpoint_config):
    response_type = endpoint_config.get('response_type', 'lambda_proxy')
    if (response_type == 'lambda_proxy'):
        return response['body'], response['statusCode'], response['headers']

    body = json.dumps(response) if response else "{}"
    return body, 200, {'Content-Type': 'application/json'}
