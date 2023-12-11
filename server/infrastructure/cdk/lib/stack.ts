import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";

import { Lambdas } from "./lambdas";
import { Authorizers } from "./authorizers";
import { KrHttpApi } from "./http-api";
import { SSM_PARAM_NAMES, SsmParams } from "./ssm-params";
import { KrCognitoUserPool } from "./cognito-user-pool";
import { Scheduler } from "./scheduler";
import { KrDomainName } from "./domain-name";

export class Stack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const domainName = new KrDomainName(this, "KrDomainName", {
      hostedZoneId: process.env.HOSTED_ZONE_ID as string,
      rootDomainName: process.env.HOSTED_ZONE_DOMAIN_NAME as string,
    });

    const cognitoUserPool = new KrCognitoUserPool(this, "KrCognitoUserPool");

    const lambdas = new Lambdas(this, "Lambdas", {
      defaultEnvVars: SSM_PARAM_NAMES,
    });

    const authorizers = new Authorizers(this, "Authorizers", {
      lambdas,
      userPool: {
        instance: cognitoUserPool.userPool,
        appClient: cognitoUserPool.mobileAppClient,
      },
    });
    new KrHttpApi(this, "KrHttpApi", {
      lambdas,
      authorizers,
      domainName,
    });

    new Scheduler(this, "Scheduler", {
      postScheduleLambda: lambdas.getByName("PostSchedule"),
      deleteScheduleLambda: lambdas.getByName("DeleteSchedule"),
      sendClippingLambda: lambdas.getByName("SendClipping"),
    });

    const ssmParams = new SsmParams(this, "SsmParams");
    ssmParams.grantRead(lambdas.getAll());
  }
}
