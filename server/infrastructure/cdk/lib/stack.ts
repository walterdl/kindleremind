import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";

import { Lambdas } from "./lambdas";
import { Authorizers } from "./authorizers";
import { KrHttpApi } from "./http-api";
import { SSM_PARAM_NAMES, SsmParams } from "./ssm-params";
import { KrCognitoUserPool } from "./cognito-user-pool";
import { Scheduler } from "./scheduler";

export class Stack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

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
    });

    new Scheduler(this, "Scheduler", {
      postScheduleLambda: lambdas.getByName("PostSchedule"),
    });

    const ssmParams = new SsmParams(this, "SsmParams");
    ssmParams.grantRead(lambdas.getAll());
  }
}
