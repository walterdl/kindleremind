import path = require("path");
import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as python from "@aws-cdk/aws-lambda-python-alpha";
import * as apigwv2 from "@aws-cdk/aws-apigatewayv2-alpha";
import { HttpLambdaIntegration } from "@aws-cdk/aws-apigatewayv2-integrations-alpha";

import { SSM_PARAM_NAMES, SsmParams } from "./ssm-params";
import { KrCognitoUserPool } from "./cognito-user-pool";

export class Stack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

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

    const ssmParams = new SsmParams(this, "SsmParams");
    ssmParams.grantRead([
      saveClippingsFunction,
      getClippingsFunction,
      postPushTokenFunction,
      deletePushTokenFunction,
      getApiKeysFunction,
      postApiKeyFunction,
      deleteApiKeyFunction,
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
  }
}
