endpoints = {
    '/clippings': {
        'post': {
            'handler_module': 'kindleremind.api.post_clippings.handler',
            'handler_func': "lambda_handler",
        },
        'get': {
            'handler_module': 'kindleremind.api.get_clippings.handler',
            'handler_func': "lambda_handler",
        }
    }
}
