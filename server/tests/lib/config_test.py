import pytest
from kindleremind.lib.config import get_config, NAMES
from .config_data import clean_env_vars, ssm_value, ssm_client, clear_ssm_instance, clear_ssm_cache


def test_uses_hardcoded_values_if_env_is_test(clean_env_vars):
    clean_env_vars['ENV'] = 'TEST'
    for name in NAMES:
        assert get_config(name) == f'{name}_test_value'


def test_uses_ssm_values_by_default(ssm_client):
    for name in NAMES:
        ssm_env_var_name = NAMES[name]['ssm_env_var']
        assert get_config(name) == ssm_value(ssm_env_var_name)


def test_gets_secure_ssm_params_with_correct_arguments(ssm_client):
    i = 0
    for name in NAMES:
        get_config(name)
        assert ssm_client.mock_calls[i].kwargs['Name'] == NAMES[name]['ssm_env_var']
        assert ssm_client.mock_calls[i].kwargs['WithDecryption'] == True
        i += 1


def test_uses_local_env_vars_if_it_is_local(clean_env_vars):
    clean_env_vars['IS_LOCAL'] = 'true'

    for name in NAMES:
        clean_env_vars[NAMES[name]['env_var']] = f'{name}_local_value'

        assert get_config(name) == f'{name}_local_value'


def test_returns_from_ssm_cache_if_available(ssm_client):
    result = get_config('mongodb_uri')
    ssm_client.get_parameter.assert_called_once()
    result2 = get_config('mongodb_uri')
    ssm_client.get_parameter.assert_called_once()
    assert result == result2


def test_throws_if_unknown_config_value_is_requested():
    with pytest.raises(KeyError) as error:
        get_config('unknown_config_value')

    assert error.value.args[0] == 'Unknown config value: unknown_config_value'
