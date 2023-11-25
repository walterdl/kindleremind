import boto3

from .service import CreateReminderScheduleService
from kindleremind.lib.config import get_config
from .storage import ReminderScheduleStorage
from kindleremind.lib.mongodb.connection import schedules as schedules_collection
from .scheduler import Scheduler

eventbridge_scheduler = boto3.client('scheduler')


def get_service(context):
    return CreateReminderScheduleService(
        int(get_config('max_schedules_per_user')),
        ReminderScheduleStorage(context, schedules_collection),
        Scheduler(
            get_config('reminder_sns_topic_arn'),
            get_config('publish_reminder_role_arn'),
            eventbridge_scheduler
        )
    )
