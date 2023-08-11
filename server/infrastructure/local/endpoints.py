endpoints = [
    {
        'route': '/clippings',
        'method': 'post',
        'handler_module': 'kindleremind.api.post_clippings.handler',
        'handler_func': "lambda_handler",
    }
]
