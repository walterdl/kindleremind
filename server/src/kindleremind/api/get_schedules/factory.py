from .service import GetSchedulesService
from .storage import Storage
from kindleremind.lib.mongodb.connection import schedules


def get_service(context):
    return GetSchedulesService(context, Storage(schedules))
