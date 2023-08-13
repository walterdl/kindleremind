import boto3
import os


NAMES = {
    'mongodb_uri': {
        'local': 'MONGODB_URI',
        'ssm': 'MONGODB_URI_SSM_NAME',
    }
}


class SsmValues():
    def __init__(self, client=None):
        self.loaded = False
        if client is None:
            self.client = boto3.client('ssm')
        else:
            self.client = client

    def load(self):
        if self.loaded:
            return

        for name in NAMES:
            if self._is_dev():
                self.__dict__[name] = self._local_value(name)
            else:
                self.__dict__[name] = self._ssm_value(name)

        self.loaded = True

    def _is_dev(self):
        return os.environ.get('ENV') == 'DEV'

    def _local_value(self, name):
        return os.environ.get(NAMES[name]['local'])

    def _ssm_value(self, name):
        response = self.client.get_parameter(
            Name=os.environ.get(NAMES[name]['ssm']), WithDecryption=True)

        return response['Parameter']['Value']


class DummySsmValues():
    def __init__(self):
        for name in NAMES:
            self.__dict__[name] = 'dummy'

    def load(self):
        ...


_instance = None


def get_ssm_values():
    global _instance

    if _instance is None:
        print('DEBUG the env', os.environ.get('ENV'))
        if os.environ.get('ENV') == 'TEST':
            _instance = DummySsmValues()
        else:
            _instance = SsmValues()
        _instance.load()

    return _instance
