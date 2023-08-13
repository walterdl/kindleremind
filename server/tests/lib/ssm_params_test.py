import pytest
from unittest.mock import Mock, patch
from kindleremind.lib.config.ssm_params import SsmValues, NAMES


@pytest.fixture()
def instance():
    client_mock = Mock()
    client_mock.get_parameter.side_effect = lambda **kwards: {
        'Parameter': {
            'Value': kwards['Name'],
        }
    }

    return SsmValues(client_mock)


def mock_envs(env):
    mock = Mock()
    mock.environ.get.side_effect = lambda x: env if x == 'ENV' else x

    return mock


@pytest.fixture()
def dev_envs():
    with patch('kindleremind.lib.config.ssm_params.os', mock_envs('DEV')):
        yield


@pytest.fixture()
def prod_envs():
    with patch('kindleremind.lib.config.ssm_params.os', mock_envs('Whatever other env')):
        yield


def test_gets_value_from_local_env_if_is_dev(instance, dev_envs):
    instance.load()
    assert instance.mongodb_uri == NAMES['mongodb_uri']['local']


def test_gets_value_from_ssm_if_is_not_dev(instance, prod_envs):
    instance.load()
    assert instance.mongodb_uri == NAMES['mongodb_uri']['ssm']


def test_does_not_load_twice(instance, prod_envs):
    instance.load()
    instance.client.get_parameter.assert_called_once()
    instance.load()
    instance.client.get_parameter.assert_called_once()
