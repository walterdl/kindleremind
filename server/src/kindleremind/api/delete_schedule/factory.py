import boto3

from .service import DeleteScheduleService
from .storage import Storage
from .scheduler import Scheduler
from kindleremind.lib.mongodb.connection import schedules
from kindleremind.lib.mongodb.id_validator import validate_mongodb_id


eventbridge_scheduler = boto3.client('scheduler')


def get_service(context):
    return DeleteScheduleService(context, Storage(schedules), validate_mongodb_id, Scheduler(eventbridge_scheduler))
