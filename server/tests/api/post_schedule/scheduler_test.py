import pytest
from unittest.mock import Mock
from datetime import datetime
import json

from kindleremind.api.post_schedule.scheduler import Scheduler


@pytest.fixture()
def schedule_input():
    return {
        'id': 'The schedule ID',
        'datetime': datetime.fromisoformat('2020-04-17T09:30:00.000Z'),
        'weekdays': ['1', '2', '4'],
    }


@pytest.fixture()
def instance():
    eventbridge_client = Mock()

    return Scheduler(
        'The SNS topic ARN',
        'The Role ARN',
        eventbridge_client,
    )


def test_sets_action_after_completion_to_none(instance, schedule_input):
    instance.schedule_reminder(schedule_input)

    assert instance.eventbridge_client.create_schedule.call_args.kwargs[
        'ActionAfterCompletion'] == 'NONE'


def test_turns_off_flexible_time_window(instance, schedule_input):
    instance.schedule_reminder(schedule_input)

    assert instance.eventbridge_client.create_schedule.call_args.kwargs[
        'FlexibleTimeWindow'] == {
            'Mode': 'OFF'
    }


def test_sets_rule_name_equal_to_scheduler_id(instance, schedule_input):
    instance.schedule_reminder(schedule_input)

    assert instance.eventbridge_client.create_schedule.call_args.kwargs[
        'Name'] == schedule_input['id']


def test_sets_schedule_expression_correctly(instance, schedule_input):
    instance.schedule_reminder(schedule_input)

    cron_expression = instance.eventbridge_client.create_schedule.call_args.kwargs[
        'ScheduleExpression']

    assert cron_expression == 'cron(30 9 ? * MON,TUE,THU *)'


def test_sets_schedule_expression_timezone_to_utc(instance, schedule_input):
    instance.schedule_reminder(schedule_input)

    assert instance.eventbridge_client.create_schedule.call_args.kwargs[
        'ScheduleExpressionTimezone'] == 'UTC'


def test_enables_new_rule(instance, schedule_input):
    instance.schedule_reminder(schedule_input)

    assert instance.eventbridge_client.create_schedule.call_args.kwargs['State'] == 'ENABLED'


def test_sends_messages_to_specified_sns_topic(instance, schedule_input):
    instance.schedule_reminder(schedule_input)
    target = instance.eventbridge_client.create_schedule.call_args.kwargs['Target']

    assert target['Arn'] == instance.sns_topic_arn


def test_includes_the_schedule_in_message_input(instance, schedule_input):
    instance.schedule_reminder(schedule_input)
    target = instance.eventbridge_client.create_schedule.call_args.kwargs['Target']

    assert target['Input'] == json.dumps({
        **schedule_input,
        'datetime': datetime.isoformat(schedule_input['datetime'])
    })


def test_uses_specified_role_to_send_the_message(instance, schedule_input):
    instance.schedule_reminder(schedule_input)
    target = instance.eventbridge_client.create_schedule.call_args.kwargs['Target']

    assert target['RoleArn'] == instance.role_arn
