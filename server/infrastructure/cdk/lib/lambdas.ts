import { Construct } from "constructs";
import path = require("path");
import * as python from "@aws-cdk/aws-lambda-python-alpha";
import * as lambda from "aws-cdk-lib/aws-lambda";

import { LambdaConfigs, LambdaConfig } from "./lambdas-config";

export class Lambdas extends Construct {
  private lambdasByName: Record<string, lambda.Function> = {};

  constructor(scope: Construct, id: string, props: Props) {
    super(scope, id);

    for (const lambdaConfig of LambdaConfigs.getAll()) {
      const lambdaConstruct = new python.PythonFunction(
        this,
        lambdaConstructName(lambdaConfig),
        {
          functionName: lambdaConfig.name,
          entry: path.resolve(__dirname, "../../../src"),
          runtime: lambda.Runtime.PYTHON_3_11,
          index: toFilePath(lambdaConfig.handlerModule),
          handler: lambdaConfig.handlerFunc,
          environment: props.defaultEnvVars,
        }
      );
      this.lambdasByName[lambdaConfig.name] = lambdaConstruct;
    }
  }

  getAll() {
    return Object.values(this.lambdasByName);
  }

  getByName(name: string) {
    return this.lambdasByName[name];
  }
}

function lambdaConstructName(lambdaConfig: LambdaConfig) {
  return `${lambdaConfig.name}Lambda`;
}

function toFilePath(handlerModule: string) {
  return handlerModule.replace(/\./g, "/") + ".py";
}

interface Props {
  defaultEnvVars: Record<string, string>;
}
