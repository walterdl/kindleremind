"""Local API Gateway for testing Lambda functions locally."""

from importlib import import_module
from flask import Flask, request
import traceback
import json
import yaml


app = Flask(__name__)


def get_lambda_specs():
    with open('../lambdas.yml') as lambda_configs_file:
        lambda_configs = yaml.load(lambda_configs_file, Loader=yaml.Loader)

    return (x for x in lambda_configs.values())


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


def format_lambda_response(response, lambda_spec):
    if (lambda_spec.get('type', 'endpoint') == 'endpoint'):
        return response.get('body', ''), response['statusCode'], response['headers']

    body = json.dumps(response) if response else "{}"
    return body, 200, {'Content-Type': 'application/json'}


for lambda_spec in get_lambda_specs():
    if 'path' not in lambda_spec or 'method' not in lambda_spec:
        continue

    @app.route(
        lambda_spec['path'],
        methods=[lambda_spec['method'].upper()],
        endpoint=f"{lambda_spec['path']}_{lambda_spec['method']}"
    )
    def handler(lambda_spec=lambda_spec):
        handler_module = import_module(lambda_spec['handler_module'])
        handler_func = getattr(
            handler_module, lambda_spec['handler_func'])

        try:
            context = None
            response = handler_func(build_event(), context)

            return format_lambda_response(response, lambda_spec)
        except Exception as error:
            body = {
                'error': str(error),
                'traceback': traceback.format_exception(error)
            }

            return body, 500, {'Content-Type': 'application/json'}
