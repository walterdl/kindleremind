endpoints = {
    '/authorizer': {
        'post': {
            'response_type': 'raw',
            'handler_module': 'kindleremind.api.authorizer.handler',
            'handler_func': "lambda_handler",
        }
    },
    '/clippings': {
        'post': {
            'response_type': 'lambda_proxy',
            'handler_module': 'kindleremind.api.post_clippings.handler',
            'handler_func': "lambda_handler",
        },
        'get': {
            'response_type': 'lambda_proxy',
            'handler_module': 'kindleremind.api.get_clippings.handler',
            'handler_func': "lambda_handler",
        }
    },
    '/push-token': {
        'post': {
            'response_type': 'lambda_proxy',
            'handler_module': 'kindleremind.api.post_push_token.handler',
            'handler_func': "lambda_handler",
        },
        'delete': {
            'response_type': 'lambda_proxy',
            'handler_module': 'kindleremind.api.delete_push_token.handler',
            'handler_func': "lambda_handler",
        }
    },
    '/api-keys': {
        'get': {
            'response_type': 'lambda_proxy',
            'handler_module': 'kindleremind.api.get_api_keys.handler',
            'handler_func': "lambda_handler",
        },
    }
}
