endpoints = {
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
        'post': {
            'response_type': 'lambda_proxy',
            'handler_module': 'kindleremind.api.post_api_key.handler',
            'handler_func': 'lambda_handler',
        },
        'delete': {
            'response_type': 'lambda_proxy',
            'handler_module': 'kindleremind.api.delete_api_key.handler',
            'handler_func': 'lambda_handler',
        }
    },
    '/schedules': {
        'post': {
            'response_type': 'lambda_proxy',
            'handler_module': 'kindleremind.api.post_schedule.handler',
            'handler_func': 'lambda_handler',
        },
    }
}
