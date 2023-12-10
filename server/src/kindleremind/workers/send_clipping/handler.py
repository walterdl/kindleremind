import json
from .factory import get_service


def handler(event, lambda_context=None):
    payload = event['Records'][0]['Sns']['Message']
    payload = json.loads(payload)
    context = {'email': payload['user']}
    service = get_service(context)
    service.send_clipping()
