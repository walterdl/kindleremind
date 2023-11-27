class Scheduler():
    def __init__(self, eventbridge_client):
        self.eventbridge_client = eventbridge_client

    def delete_scheduled_reminder(self, reminder_id):
        self.eventbridge_client.delete_schedule(Name=reminder_id)
