import { Construct } from "constructs";
import * as sns from "aws-cdk-lib/aws-sns";
import * as iam from "aws-cdk-lib/aws-iam";
import * as eventBridge from "aws-cdk-lib/aws-events";

export class Scheduler extends Construct {
  readonly eventBus: eventBridge.IEventBus;
  readonly publishRemindersIamRole: iam.Role;
  readonly remindersSnsTopic: sns.Topic;

  constructor(scope: Construct, id: string) {
    super(scope, id);

    this.eventBus = eventBridge.EventBus.fromEventBusName(
      this,
      "DefaultEventBus",
      "default"
    );

    this.remindersSnsTopic = new sns.Topic(this, "RemindersSnsTopic", {
      displayName: "KrRemindersSnsTopic",
      topicName: "KrRemindersSnsTopic",
    });
    const publishRemindersIamPolicy = new iam.Policy(
      this,
      "PublishRemindersIamPolicy",
      {
        statements: [
          new iam.PolicyStatement({
            effect: iam.Effect.ALLOW,
            actions: ["sns:Publish"],
            resources: [this.remindersSnsTopic.topicArn],
          }),
        ],
        policyName: "PublishToKrRemindersTopic",
      }
    );
    this.publishRemindersIamRole = new iam.Role(
      this,
      "PublishRemindersIamRole",
      {
        assumedBy: new iam.ServicePrincipal("scheduler.amazonaws.com"),
        description:
          "Role for publishing reminders to KindleRemindRemindersTopic from EventBridge Scheduler",
        roleName: "PublishKrReminders",
      }
    );
    publishRemindersIamPolicy.attachToRole(this.publishRemindersIamRole);
  }
}
