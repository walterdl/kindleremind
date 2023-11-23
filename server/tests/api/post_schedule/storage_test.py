from unittest.mock import Mock
import pytest
from datetime import datetime
from pymongo.results import InsertOneResult


from kindleremind.api.post_schedule.storage import ReminderScheduleStorage
from tests.api.common_fixtures import app_context, doc_bid, doc_id


@pytest.fixture()
def schedules_count():
    return 2


@pytest.fixture()
def schedule_input():
    return {
        'datetime': datetime.fromisoformat('2020-04-17T09:30:00.000Z'),
        'weekdays': ['1', '2'],
    }


@pytest.fixture()
def instance(app_context, schedules_count, doc_bid):
    def dummy_insert_one(doc):
        doc['_id'] = doc_bid

        return InsertOneResult(doc_bid, True)

    insert_one = Mock(side_effect=dummy_insert_one)
    storage = Mock(count_documents=Mock(
        return_value=schedules_count), insert_one=insert_one)

    return ReminderScheduleStorage(app_context, storage)


def test_queries_schedules_count_of_user(instance, app_context):
    instance.get_schedules_count()

    instance.collection.count_documents.assert_called_once_with({
        'user': app_context['email']
    })


def test_returns_schedules_count(instance, schedules_count):
    result = instance.get_schedules_count()

    assert result == schedules_count


def test_creates_schedule_with_user_context(instance, schedule_input):
    instance.create(schedule_input)

    instance.collection.insert_one.assert_called_once_with({
        'user': instance.context['email'],
        'datetime': schedule_input['datetime'],
        'weekdays': schedule_input['weekdays'],
    })


def test_returns_created_schedule_with_id_as_string(instance, schedule_input, doc_id, app_context):
    result = instance.create(schedule_input)

    assert result != schedule_input
    assert result == {
        'id': doc_id,
        'datetime': schedule_input['datetime'],
        'weekdays': schedule_input['weekdays'],
        'user': app_context['email'],
    }
