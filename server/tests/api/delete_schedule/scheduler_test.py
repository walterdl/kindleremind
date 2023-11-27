from unittest.mock import Mock
import pytest

from kindleremind.api.delete_schedule.scheduler import Scheduler


@pytest.fixture()
def instance():
    return Scheduler(eventbridge_client=Mock())


def test_delete_scheduled_reminder_using_given_id(instance):
    instance.delete_scheduled_reminder('The reminder ID')

    instance.eventbridge_client.delete_schedule.assert_called_once_with(
        Name='The reminder ID')
