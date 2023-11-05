import json


def get_handler_wrapper(app_handler, build_app_context):
    """
    Wraps an application handler function with additional context and formatting.

    This function is a higher-order function that takes an app handler and a context builder
    function as arguments. It returns a new handler that enriches the event with application-specific
    context and ensures the response is properly formatted as a JSON response suitable for
    AWS Lambda proxy integration in API Gateway.
    """

    def handler_wrapper(event, context):
        event['app_context'] = build_app_context(event)
        result = app_handler(event, context)

        return _format_result(result)

    return handler_wrapper


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
