from datetime import datetime
import json


def handler(event=None, context=None):
    return {
        'statusCode': 200,
        'body': json.dumps({
            'date': datetime.now().isoformat()
        }),
        'headers': {
            'Content-Type': 'application/json',
        }
    }
