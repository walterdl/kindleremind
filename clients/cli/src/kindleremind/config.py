from os import environ, path
import json
from .exceptions import AppException

var_sources = {
    'server_url': {
        'env': 'SERVER_URL',
        'config_file': 'serverUrl',
        'cli_arg': 'server_url'
    },
    'server_api_key': {
        'env': 'SERVER_API_KEY',
        'config_file': 'serverApiKey',
        'cli_arg': 'server_api_key'
    },
}


class _Config():
    def __init__(self, cli_args={}):
        self._set_vars_by_priority([
            self._cli_args(cli_args),
            self._env_vars(),
            self._config_file_vars()
        ])

    def _set_vars_by_priority(self, vars_by_priority):
        first_priority = vars_by_priority[0]
        second_priority = vars_by_priority[1]
        last_priority = vars_by_priority[2]

        for var_name in var_sources:
            if var_name in first_priority:
                self.__dict__[var_name] = first_priority[var_name]
            elif var_name in second_priority:
                self.__dict__[var_name] = second_priority[var_name]
            elif var_name in last_priority:
                self.__dict__[var_name] = last_priority[var_name]
            else:
                raise AppException('No configuration found for ' + var_name)

    def _cli_args(self, raw_values):
        result = {}

        for var_name in var_sources:
            cli_arg_name = var_sources[var_name]['cli_arg']
            if cli_arg_name in raw_values and raw_values[cli_arg_name]:
                result[var_name] = raw_values[cli_arg_name]

        return result

    def _env_vars(self):
        result = {}

        for var_name in var_sources:
            val = environ.get(var_sources[var_name]['env'])
            if val:
                result[var_name] = val

        return result

    def _config_file_vars(self):
        result = {}
        config_file_path = path.join(
            path.expanduser('~'), '.kindleremind.json')

        try:
            with open(config_file_path, 'r') as config_file:
                config = json.loads(config_file.read())
                for var_name in var_sources:
                    config_file_var_name = var_sources[var_name]['config_file']
                    if config_file_var_name in config and config[config_file_var_name]:
                        result[var_name] = config[config_file_var_name]
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass

        return result


# type: _Config
config = None


def init_config(cli_args={}):
    global config

    if config:
        return

    if environ.get('ENV') == 'TEST':
        # For testing purposes use dummy values.
        cli_args = {}
        for var_name in var_sources:
            cli_args[var_sources[var_name]['cli_arg']] = 'test_' + var_name

    config = _Config(cli_args)
