import json


def lambda_handler(event, context=None):
    json_body = json.loads(event['body'])
    print('json_body', json_body)

    return {
        'statusCode': 201,
        'body': json.dumps({'message': 'Hello from Lambda!'}),
        'headers': {
            'Content-Type': 'application/json',
        }
    }
