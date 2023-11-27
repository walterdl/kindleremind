from .service import DeleteScheduleService
from .storage import Storage
from kindleremind.lib.mongodb.connection import schedules
from kindleremind.lib.mongodb.id_validator import validate_mongodb_id


def get_service(context):
    return DeleteScheduleService(context, Storage(schedules), validate_mongodb_id)
