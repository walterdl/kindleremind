from os import environ
import boto3

NAMES = {
    'mongodb_uri': {
        'env_var': 'MONGODB_URI',
        'ssm_env_var': 'MONGODB_URI_SSM_NAME',
    },
    'api_key': {
        'env_var': 'API_KEY',
        'ssm_env_var': 'API_KEY_SSM_NAME',
    },
    'max_schedules_per_user': {
        'env_var': 'MAX_SCHEDULES_PER_USER',
    },
    'reminder_sns_topic_arn': {
        'env_var': 'REMINDER_SNS_TOPIC_ARN',
    },
    'publish_reminder_role_arn': {
        'env_var': 'PUBLISH_REMINDER_ROLE_ARN',
    },
    'firebase_service_account_private_key': {
        'env_var': 'FIREBASE_SERVICE_ACCOUNT_PRIVATE_KEY',
        'ssm_env_var': 'FIREBASE_SERVICE_ACCOUNT_PRIVATE_KEY_SSM_NAME',
    }
}


def get_config(name):
    _validate_config_name(name)

    if _is_test():
        return f'{name}_test_value'

    config_sources = NAMES.get(name)

    if _is_local():
        return environ.get(config_sources['env_var'])

    if name in get_config._cache:
        return get_config._cache[name]

    # Env var takes precedence over SSM param
    if config_sources['env_var'] in environ:
        value = environ.get(config_sources['env_var'])
    else:
        value = _get_ssm_value(
            environ.get(config_sources['ssm_env_var'])
        )

    # Store in cache for future calls, avoiding unnecessary SSM calls.
    get_config._cache[name] = value

    return get_config._cache[name]


get_config._cache = {}


def _validate_config_name(name):
    if name not in NAMES:
        raise KeyError(f'Unknown config value: {name}')


def _get_ssm_value(ssm_name):
    ssm_response = _ssm_client().get_parameter(
        Name=ssm_name,
        WithDecryption=True
    )
    return ssm_response['Parameter']['Value']


def _ssm_client():
    if _is_local():
        return None

    if _ssm_client._instance:
        return _ssm_client._instance

    _ssm_client._instance = boto3.client('ssm')
    return _ssm_client._instance


_ssm_client._instance = None


def _is_test():
    return environ.get('ENV') == 'TEST'


def _is_local():
    return environ.get('IS_LOCAL') == 'true'
