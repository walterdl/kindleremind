import path = require("path");
import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as python from "@aws-cdk/aws-lambda-python-alpha";
import * as apigwv2 from "@aws-cdk/aws-apigatewayv2-alpha";
import { HttpLambdaIntegration } from "@aws-cdk/aws-apigatewayv2-integrations-alpha";
import {
  HttpLambdaAuthorizer,
  HttpLambdaResponseType,
} from "@aws-cdk/aws-apigatewayv2-authorizers-alpha";
import * as iam from "aws-cdk-lib/aws-iam";

import { SSM_PARAM_NAMES, SsmParams } from "./ssm-params";
import { KrCognitoUserPool } from "./cognito-user-pool";
import { Scheduler } from "./scheduler";

export class Stack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const scheduler = new Scheduler(this, "Scheduler");

    const apiKeyAuthorizerFunction = new python.PythonFunction(
      this,
      "ApiKeyAuthorizerFunction",
      {
        entry: path.resolve(__dirname, "../../../src"),
        runtime: lambda.Runtime.PYTHON_3_11,
        index: "kindleremind/api/api_key_authorizer/handler.py",
        handler: "lambda_handler",
        environment: {
          ...SSM_PARAM_NAMES,
        },
      }
    );
    const apiKeyLambdaAuthorizer = new HttpLambdaAuthorizer(
      "ApiKeyLambdaAuthorizer",
      apiKeyAuthorizerFunction,
      {
        authorizerName: "ApiKeyAuthorizer",
        responseTypes: [HttpLambdaResponseType.SIMPLE],
        identitySource: ["$request.header.Authorization"],
      }
    );

    const saveClippingsFunction = new python.PythonFunction(
      this,
      "SaveClippingsFunction",
      {
        entry: path.resolve(__dirname, "../../../src"),
        runtime: lambda.Runtime.PYTHON_3_11,
        index: "kindleremind/api/post_clippings/handler.py",
        handler: "lambda_handler",
        environment: {
          ...SSM_PARAM_NAMES,
        },
      }
    );
    const saveClippingsIntegration = new HttpLambdaIntegration(
      "SaveClippingsIntegration",
      saveClippingsFunction
    );

    const getClippingsFunction = new python.PythonFunction(
      this,
      "GetClippingsFunction",
      {
        entry: path.resolve(__dirname, "../../../src"),
        runtime: lambda.Runtime.PYTHON_3_11,
        index: "kindleremind/api/get_clippings/handler.py",
        handler: "lambda_handler",
        environment: {
          ...SSM_PARAM_NAMES,
        },
      }
    );
    const getClippingsIntegration = new HttpLambdaIntegration(
      "getClippingsIntegration",
      getClippingsFunction
    );

    const statusFunction = new python.PythonFunction(this, "statusFunction", {
      entry: path.resolve(__dirname, "../../../src"),
      runtime: lambda.Runtime.PYTHON_3_11,
      index: "kindleremind/api/status.py",
      handler: "handler",
    });
    const statusIntegration = new HttpLambdaIntegration(
      "statusIntegration",
      statusFunction
    );

    const postPushTokenFunction = new python.PythonFunction(
      this,
      "PostPushTokenFunction",
      {
        entry: path.resolve(__dirname, "../../../src"),
        runtime: lambda.Runtime.PYTHON_3_11,
        index: "kindleremind/api/post_push_token/handler.py",
        handler: "lambda_handler",
        environment: {
          ...SSM_PARAM_NAMES,
        },
      }
    );
    const postPushTokenIntegration = new HttpLambdaIntegration(
      "PostPushTokenIntegration",
      postPushTokenFunction
    );

    const deletePushTokenFunction = new python.PythonFunction(
      this,
      "DeletePushTokenFunction",
      {
        entry: path.resolve(__dirname, "../../../src"),
        runtime: lambda.Runtime.PYTHON_3_11,
        index: "kindleremind/api/delete_push_token/handler.py",
        handler: "lambda_handler",
        environment: {
          ...SSM_PARAM_NAMES,
        },
      }
    );
    const deletePushTokenIntegration = new HttpLambdaIntegration(
      "DeletePushTokenIntegration",
      deletePushTokenFunction
    );

    const getApiKeysFunction = new python.PythonFunction(
      this,
      "GetApiKeysFunction",
      {
        entry: path.resolve(__dirname, "../../../src"),
        runtime: lambda.Runtime.PYTHON_3_11,
        index: "kindleremind/api/get_api_keys/handler.py",
        handler: "lambda_handler",
        environment: {
          ...SSM_PARAM_NAMES,
        },
      }
    );
    const getApiKeysIntegration = new HttpLambdaIntegration(
      "GetApiKeysIntegration",
      getApiKeysFunction
    );

    const postApiKeyFunction = new python.PythonFunction(
      this,
      "PostApiKeyFunction",
      {
        entry: path.resolve(__dirname, "../../../src"),
        runtime: lambda.Runtime.PYTHON_3_11,
        index: "kindleremind/api/post_api_key/handler.py",
        handler: "lambda_handler",
        environment: {
          ...SSM_PARAM_NAMES,
        },
      }
    );
    const postApiKeyIntegration = new HttpLambdaIntegration(
      "PostApiKeyIntegration",
      postApiKeyFunction
    );

    const deleteApiKeyFunction = new python.PythonFunction(
      this,
      "DeleteApiKeyFunction",
      {
        entry: path.resolve(__dirname, "../../../src"),
        runtime: lambda.Runtime.PYTHON_3_11,
        index: "kindleremind/api/delete_api_key/handler.py",
        handler: "lambda_handler",
        environment: {
          ...SSM_PARAM_NAMES,
        },
      }
    );
    const deleteApiKeyIntegration = new HttpLambdaIntegration(
      "DeleteApiKeyIntegration",
      deleteApiKeyFunction
    );

    const postScheduleFunction = new python.PythonFunction(
      this,
      "PostScheduleFunction",
      {
        entry: path.resolve(__dirname, "../../../src"),
        runtime: lambda.Runtime.PYTHON_3_11,
        index: "kindleremind/api/post_schedule/handler.py",
        handler: "lambda_handler",
        environment: {
          ...SSM_PARAM_NAMES,
          MAX_SCHEDULES_PER_USER: "2",
          REMINDER_SNS_TOPIC_ARN: scheduler.remindersSnsTopic.topicArn,
          PUBLISH_REMINDER_ROLE_ARN: scheduler.publishRemindersIamRole.roleArn,
        },
      }
    );
    const postScheduleIntegration = new HttpLambdaIntegration(
      "PostScheduleIntegration",
      postScheduleFunction
    );

    scheduler.eventBus.grantPutEventsTo(postScheduleFunction);

    postScheduleFunction.addToRolePolicy(
      new iam.PolicyStatement({
        effect: iam.Effect.ALLOW,
        actions: ["scheduler:CreateSchedule"],
        resources: ["*"],
      })
    );
    postScheduleFunction.addToRolePolicy(
      new iam.PolicyStatement({
        effect: iam.Effect.ALLOW,
        actions: ["iam:PassRole"],
        resources: [scheduler.publishRemindersIamRole.roleArn],
        conditions: {
          StringEquals: {
            "iam:PassedToService": "scheduler.amazonaws.com",
          },
        },
      })
    );

    const ssmParams = new SsmParams(this, "SsmParams");
    ssmParams.grantRead([
      apiKeyAuthorizerFunction,
      saveClippingsFunction,
      getClippingsFunction,
      postPushTokenFunction,
      deletePushTokenFunction,
      getApiKeysFunction,
      postApiKeyFunction,
      deleteApiKeyFunction,
      postScheduleFunction,
    ]);

    const cognitoUserPool = new KrCognitoUserPool(this, "KrCognitoUserPool");

    const httpApi = new apigwv2.HttpApi(this, "HttpApi", {
      apiName: "KindleRemindApi",
      createDefaultStage: false,
      disableExecuteApiEndpoint: false,
      defaultAuthorizer: cognitoUserPool.authorizer,
    });

    new apigwv2.HttpStage(this, "Stage", {
      httpApi,
      stageName: "v1",
      autoDeploy: true,
    });
    httpApi.addRoutes({
      path: "/clippings",
      methods: [apigwv2.HttpMethod.POST],
      integration: saveClippingsIntegration,
      authorizer: apiKeyLambdaAuthorizer,
    });
    httpApi.addRoutes({
      path: "/clippings",
      methods: [apigwv2.HttpMethod.GET],
      integration: getClippingsIntegration,
    });
    httpApi.addRoutes({
      path: "/status",
      methods: [apigwv2.HttpMethod.GET],
      integration: statusIntegration,
      authorizer: new apigwv2.HttpNoneAuthorizer(),
    });
    httpApi.addRoutes({
      path: "/push-token",
      methods: [apigwv2.HttpMethod.POST],
      integration: postPushTokenIntegration,
    });
    httpApi.addRoutes({
      path: "/push-token",
      methods: [apigwv2.HttpMethod.DELETE],
      integration: deletePushTokenIntegration,
    });
    httpApi.addRoutes({
      path: "/api-keys",
      methods: [apigwv2.HttpMethod.GET],
      integration: getApiKeysIntegration,
    });
    httpApi.addRoutes({
      path: "/api-keys",
      methods: [apigwv2.HttpMethod.POST],
      integration: postApiKeyIntegration,
    });
    httpApi.addRoutes({
      path: "/api-keys",
      methods: [apigwv2.HttpMethod.DELETE],
      integration: deleteApiKeyIntegration,
    });
    httpApi.addRoutes({
      path: "/schedules",
      methods: [apigwv2.HttpMethod.POST],
      integration: postScheduleIntegration,
    });
  }
}
