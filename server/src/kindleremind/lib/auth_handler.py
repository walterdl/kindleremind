import json


def auth_handler(handler):
    def handler_wrapper(event, context=None):
        event['app_context'] = _build_app_context(event)
        result = handler(event, context)

        return _format_result(result)
        # TODO: Add error handling

    return handler_wrapper


def _build_app_context(event):
    return {
        'email': event['requestContext']['authorizer']['jwt']['claims']['email']
    }


def _format_result(raw_result):
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        }
    }

    if raw_result != None:
        response['body'] = json.dumps(raw_result)

    return response
