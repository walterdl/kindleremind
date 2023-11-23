import json
from datetime import datetime

from .cron import generate_cron_expression


class Scheduler:
    def __init__(self, sns_topic_arn, role_arn, eventbridge_client):
        self.sns_topic_arn = sns_topic_arn
        self.role_arn = role_arn
        self.eventbridge_client = eventbridge_client

    def schedule_reminder(self, schedule):
        self.eventbridge_client.create_schedule(
            ActionAfterCompletion='NONE',
            FlexibleTimeWindow={
                'Mode': 'OFF'
            },
            Name=schedule['id'],
            ScheduleExpression=generate_cron_expression(schedule),
            ScheduleExpressionTimezone='UTC',
            State='ENABLED',
            Target={
                'Arn': self.sns_topic_arn,
                'Input': json.dumps({
                    **schedule,
                    'datetime': datetime.isoformat(schedule['datetime'])
                }),
                'RoleArn': self.role_arn,
            }
        )
