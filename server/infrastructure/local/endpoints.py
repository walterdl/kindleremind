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
    '/authorizer': {
        'post': {
            'response_type': 'raw',
            'handler_module': 'kindleremind.api.authorizer.handler',
            'handler_func': "lambda_handler",
        }
    }
}
