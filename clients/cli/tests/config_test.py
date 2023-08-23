from unittest.mock import patch, mock_open, Mock
import pytest
import json
from .config_data import clean_env_vars, env_vars, env_var_value, cli_args, cli_arg_value, config_file_vars, config_file_var_value
from kindleremind.config import var_sources, _Config
from kindleremind.exceptions import AppException


def test_uses_cli_argument_as_first_choice(env_vars, config_file_vars, cli_args):
    config = _Config(cli_args)

    for var_name in var_sources:
        assert config.__dict__[var_name] == cli_arg_value(var_name)


def test_uses_env_variable_as_second_choice(env_vars, config_file_vars):
    config = _Config()

    for var_name in var_sources:
        assert config.__dict__[var_name] == env_var_value(var_name)


def test_uses_config_file_as_third_choice(config_file_vars):
    config = _Config()

    for var_name in var_sources:
        assert config.__dict__[var_name] == config_file_var_value(var_name)


def test_ignores_config_file_if_it_does_not_exist(config_file_vars):
    config_file_vars['open_mock'].side_effect = FileNotFoundError
    with pytest.raises(Exception) as error:
        _Config()

    assert isinstance(error.value, AppException)


def test_ignores_config_file_if_it_cannot_be_unmarshalled(config_file_vars):
    config_file_vars['open_mock'].return_value.read.side_effect = lambda: 'Invalid JSON'
    with pytest.raises(Exception) as error:
        _Config()

    assert isinstance(error.value, AppException)


def test_ignores_config_file_if_it_is_not_dict(config_file_vars):
    config_file_vars['open_mock'].return_value.read.side_effect = lambda: json.dumps(
        'A simple string')
    with pytest.raises(Exception) as error:
        _Config()

    assert isinstance(error.value, AppException)


def test_throws_application_error_if_no_config_value_is_found():
    with pytest.raises(Exception) as error:
        _Config()
    assert isinstance(error.value, AppException)
