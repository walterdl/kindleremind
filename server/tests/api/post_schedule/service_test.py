import pytest
from unittest.mock import Mock
from datetime import datetime

from kindleremind.api.post_schedule.service import CreateReminderScheduleService


@pytest.fixture()
def schedule():
    return {
        'datetime': '2020-01-01T09:00:00Z',
        'weekdays': ['1', '2', '3', '4', '5'],
    }


@pytest.fixture()
def schedule_record():
    return {
        'id': 1,
        # More fields of the schedule record...
    }


@pytest.fixture()
def instance(schedule_record):
    storage = Mock(
        get_schedules_count=Mock(return_value=1),
        create=Mock(return_value=schedule_record),
    )
    scheduler = Mock()

    return CreateReminderScheduleService(2, storage, scheduler)


def test_throws_if_cannot_create_more_due_to_schedules_limit(instance, schedule):
    # The user has already reached the limit.
    instance.storage.get_schedules_count.return_value = instance.schedules_limit

    with pytest.raises(Exception) as exception:
        instance.create(schedule)

    assert exception.value.args[0] == 'Schedules limit reached'


def test_creates_schedule_using_storage(instance, schedule):
    instance.create(schedule)

    instance.storage.create.assert_called_once_with({
        'datetime': datetime.fromisoformat(schedule['datetime']),
        'weekdays': schedule['weekdays'],
    })


def test_creates_scheduled_notification_using_notification_scheduler(instance, schedule, schedule_record):
    instance.create(schedule)

    instance.scheduler.schedule_notification.assert_called_once_with(
        schedule_record)


def test_returns_created_schedule_record(instance, schedule, schedule_record):
    result = instance.create(schedule)

    assert result == schedule_record
