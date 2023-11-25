import { Construct } from "constructs";
import * as sns from "aws-cdk-lib/aws-sns";
import * as iam from "aws-cdk-lib/aws-iam";
import * as eventBridge from "aws-cdk-lib/aws-events";
import * as lambda from "aws-cdk-lib/aws-lambda";

export class Scheduler extends Construct {
  private eventBus: eventBridge.IEventBus;
  private publishRemindersIamPolicy: iam.Policy;
  private publishRemindersIamRole: iam.Role;
  private remindersSnsTopic: sns.Topic;

  constructor(scope: Construct, id: string, props: Props) {
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

    this.publishRemindersIamPolicy = new iam.Policy(
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
    this.publishRemindersIamPolicy.attachToRole(this.publishRemindersIamRole);

    this.grantPermissionsToPostSchedules(props.postScheduleLambda);
  }

  private grantPermissionsToPostSchedules(postScheduleLambda: lambda.Function) {
    postScheduleLambda.addEnvironment("MAX_SCHEDULES_PER_USER", "2");
    postScheduleLambda.addEnvironment(
      "REMINDER_SNS_TOPIC_ARN",
      this.remindersSnsTopic.topicArn
    );
    postScheduleLambda.addEnvironment(
      "PUBLISH_REMINDER_ROLE_ARN",
      this.publishRemindersIamRole.roleArn
    );
    this.eventBus.grantPutEventsTo(postScheduleLambda);

    postScheduleLambda.addToRolePolicy(
      new iam.PolicyStatement({
        effect: iam.Effect.ALLOW,
        actions: ["scheduler:CreateSchedule"],
        resources: ["*"],
      })
    );
    postScheduleLambda.addToRolePolicy(
      new iam.PolicyStatement({
        effect: iam.Effect.ALLOW,
        actions: ["iam:PassRole"],
        resources: [this.publishRemindersIamRole.roleArn],
        conditions: {
          StringEquals: {
            "iam:PassedToService": "scheduler.amazonaws.com",
          },
        },
      })
    );
  }
}

interface Props {
  postScheduleLambda: lambda.Function;
}
