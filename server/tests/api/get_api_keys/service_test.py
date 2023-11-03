import pytest
from unittest.mock import Mock
from datetime import datetime
import copy

from kindleremind.api.get_api_keys.service import GetApiKeysService


@pytest.fixture
def api_keys():
    return [
        {
            'name': 'Api Key 1',
            'value': 'value-1',
            'createdAt': datetime.fromisoformat('2023-11-04T09:00:00Z')
        },
        {
            'name': 'Api Key 2',
            'value': 'value-2',
            'createdAt': datetime.fromisoformat('2023-11-07T10:00:00Z')
        }
    ]


@pytest.fixture
def instance(api_keys):
    storage = Mock()
    storage.get_api_keys.return_value = api_keys

    return GetApiKeysService(storage)


def test_formats_date_to_iso_format(instance, api_keys):
    api_keys = copy.deepcopy(api_keys)
    result = instance.get_api_keys()

    for (i, api_key) in enumerate(api_keys):
        assert result[i]['createdAt'] == api_key['createdAt'].isoformat()
