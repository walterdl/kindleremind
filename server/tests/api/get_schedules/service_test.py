from datetime import datetime
from unittest.mock import Mock
import pytest

from kindleremind.api.get_schedules.service import GetSchedulesService
from tests.api.common_fixtures import app_context


@pytest.fixture()
def schedules():
    return [
        {
            "id": '1',
            "datetime": datetime.now(),
            "weekdays": ["1", "5"]
        },
        {
            "id": '2',
            "datetime": datetime.now(),
            "weekdays": ["1"]
        }
    ]


@pytest.fixture()
def instance(app_context, schedules):
    storage = Mock(get_user_schedules=Mock(return_value=schedules))

    return GetSchedulesService(app_context, storage)


def test_gets_schedules_of_user(instance, app_context, schedules):
    instance.get_schedules()

    instance.storage.get_user_schedules.assert_called_once_with(
        app_context['email'])


def test_returns_schedules_from_storage(instance,  schedules):
    result = instance.get_schedules()

    assert result == schedules
