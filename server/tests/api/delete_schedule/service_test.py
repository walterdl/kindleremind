from unittest.mock import Mock
import pytest

from kindleremind.api.delete_schedule.service import DeleteScheduleService
from tests.api.common_fixtures import app_context, doc_id
from kindleremind.lib.mongodb.id_validator import validate_mongodb_id


@pytest.fixture()
def instance(app_context):
    return DeleteScheduleService(context=app_context, storage=Mock(), validate_storage_id=validate_mongodb_id)


def test_throws_error_if_schedule_id_is_invalid(instance):
    with pytest.raises(ValueError):
        instance.delete_schedule("blabla")


def test_delete_schedule_of_user_identified_by_given_id(instance, app_context, doc_id):
    instance.delete_schedule(doc_id)

    instance.storage.delete_schedule.assert_called_once_with({
        "id": doc_id,
        "user": app_context['email'],
    })
