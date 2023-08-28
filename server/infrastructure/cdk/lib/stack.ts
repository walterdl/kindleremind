import path = require("path");
import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as python from "@aws-cdk/aws-lambda-python-alpha";
import * as apigwv2 from "@aws-cdk/aws-apigatewayv2-alpha";
import {
  HttpLambdaAuthorizer,
  HttpLambdaResponseType,
} from "@aws-cdk/aws-apigatewayv2-authorizers-alpha";
import { HttpLambdaIntegration } from "@aws-cdk/aws-apigatewayv2-integrations-alpha";

import { SSM_PARAM_NAMES, SsmParams } from "./ssm-params";

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

    const authorizerFunction = new python.PythonFunction(
      this,
      "AuthorizerFunction",
      {
        entry: path.resolve(__dirname, "../../../src"),
        runtime: lambda.Runtime.PYTHON_3_11,
        index: "kindleremind/api/authorizer/handler.py",
        handler: "lambda_handler",
        environment: {
          ...SSM_PARAM_NAMES,
        },
      }
    );
    const authorizer = new HttpLambdaAuthorizer(
      "Authorizer",
      authorizerFunction,
      {
        identitySource: ["$request.header.Authorization"],
        responseTypes: [HttpLambdaResponseType.SIMPLE],
        resultsCacheTtl: cdk.Duration.minutes(40),
      }
    );

    const ssmParams = new SsmParams(this, "SsmParams");
    ssmParams.grantRead([
      saveClippingsFunction,
      getClippingsFunction,
      authorizerFunction,
    ]);

    const httpApi = new apigwv2.HttpApi(this, "HttpApi", {
      apiName: "KindleRemindApi",
      createDefaultStage: false,
      disableExecuteApiEndpoint: false,
      defaultAuthorizer: authorizer,
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
    });
  }
}
