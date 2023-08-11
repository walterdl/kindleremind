"""Local API Gateway for testing Lambda functions locally."""

from importlib import import_module
from flask import Flask, request
from endpoints import endpoints

app = Flask(__name__)

for endpoint in endpoints:
    @app.route(endpoint['route'], methods=[endpoint['method']])
    def handler():
        handler_module = import_module(endpoint['handler_module'])
        handler_func = getattr(handler_module, endpoint['handler_func'])

        try:
            response = handler_func(build_event())
            return response['body'], response['statusCode'], response['headers']
        except Exception as e:
            return str(e), 500, {'Content-Type': 'text/plain'}


def build_event():
    return {
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
