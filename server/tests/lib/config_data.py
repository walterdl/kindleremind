from kindleremind.lib.config import get_config, NAMES, _ssm_client
from unittest.mock import Mock, patch
import pytest


@pytest.fixture(autouse=True)
def clean_env_vars():
    env_vars = {}
    for name in NAMES:
        ssm_env_var_name = NAMES[name]['ssm_env_var']
        env_vars[ssm_env_var_name] = ssm_env_var_name

    with patch.dict('kindleremind.lib.config.environ', env_vars, clear=True) as environ:
        yield environ


@pytest.fixture(autouse=True)
def ssm_client():
    ssm_client = Mock()
    ssm_client.get_parameter.side_effect = lambda *args, **kwargs: {
        'Parameter': {
            'Value': ssm_value(kwargs['Name'])
        }
    }

    boto3 = Mock()
    boto3.client.return_value = ssm_client

    with patch('kindleremind.lib.config.boto3', boto3):
        yield ssm_client


def ssm_value(ssm_var_name):
    return f'{ssm_var_name}_value'


@pytest.fixture(autouse=True)
def clear_ssm_instance():
    _ssm_client._instance = None


@pytest.fixture(autouse=True)
def clear_ssm_cache():
    get_config._cache = dict()
