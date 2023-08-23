from unittest.mock import patch, mock_open, Mock
import pytest
import json
from kindleremind.config import var_sources


@pytest.fixture(autouse=True)
def clean_env_vars():
    environ_mock = Mock()
    environ_mock.get.side_effect = lambda _: None

    with patch('kindleremind.config.environ', environ_mock):
        yield environ_mock


@pytest.fixture()
def env_vars(clean_env_vars):
    env_vars = {}

    for var_name in var_sources:
        env_vars[var_sources[var_name]['env']] = env_var_value(var_name)

    clean_env_vars.get.side_effect = lambda key: env_vars[key]
    yield


def env_var_value(var_name):
    return f'env_{var_name}'


@pytest.fixture()
def config_file_vars():
    config_file = {}
    for var_name in var_sources:
        config_file[var_sources[var_name]
                    ['config_file']] = config_file_var_value(var_name)

    open_mock = mock_open(read_data=json.dumps(config_file))
    with patch('builtins.open', open_mock):
        yield {'open_mock': open_mock}


def config_file_var_value(var_name):
    return f'config_file_{var_name}'


@pytest.fixture()
def cli_args():
    cli_args = {}
    for var_name in var_sources:
        cli_args[var_sources[var_name]['cli_arg']] = cli_arg_value(var_name)

    return cli_args


def cli_arg_value(var_name):
    return f'cli_arg_{var_name}'
