import path = require("path");
import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as python from "@aws-cdk/aws-lambda-python-alpha";
import * as apigwv2 from "@aws-cdk/aws-apigatewayv2-alpha";
import { HttpLambdaIntegration } from "@aws-cdk/aws-apigatewayv2-integrations-alpha";

export class Stack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const saveClippingsFunction = new python.PythonFunction(
      this,
      "SaveClippingsFunction",
      {
        entry: path.resolve(__dirname, "../../../"),
        runtime: lambda.Runtime.PYTHON_3_11,
        index: "src/api/post_clippings/handler.py",
        handler: "lambda_handler",
        bundling: {
          assetExcludes: ["infrastructure", ".env", ".vscode"],
        },
      }
    );

    const saveClippingsIntegration = new HttpLambdaIntegration(
      "SaveClippingsIntegration",
      saveClippingsFunction
    );
    const httpApi = new apigwv2.HttpApi(this, "HttpApi", {
      createDefaultStage: false,
      disableExecuteApiEndpoint: false,
    });
    new apigwv2.HttpStage(this, "Stage", {
      httpApi,
      stageName: "v1",
    });
    httpApi.addRoutes({
      path: "/clippings",
      methods: [apigwv2.HttpMethod.POST],
      integration: saveClippingsIntegration,
    });
  }
}
