import os
from .ssm_params import get_ssm_values


class _Config():
    def __init__(self):
        ssm_values = get_ssm_values()
        self.mongodb_uri = ssm_values.mongodb_uri
        self.authorizer_token = os.environ.get('AUTHORIZER_TOKEN')


config = _Config()
