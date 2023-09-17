import json

from .factory import get_service


def lambda_handler(event, _context=None):
    push_token = event['queryStringParameters'].get('push-token', None)

    try:
        get_service().delete_push_token(push_token)

        return {
            'statusCode': 200,
            'body': json.dumps({'success': True}),
            'headers': {
                'Content-Type': 'application/json',
            }
        }
    except Exception as error:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(error)}),
            'headers': {
                'Content-Type': 'application/json',
            }
        }
