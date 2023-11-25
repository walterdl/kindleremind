import { Construct } from "constructs";
import { HttpLambdaIntegration } from "@aws-cdk/aws-apigatewayv2-integrations-alpha";

import { LambdaConfigs, LambdaConfig, Auth } from "./lambdas-config";
import { Lambdas } from "./lambdas";
import {
  HttpApi,
  IHttpRouteAuthorizer,
  HttpStage,
} from "@aws-cdk/aws-apigatewayv2-alpha";
import { Authorizers } from "./authorizers";

export class KrHttpApi extends Construct {
  constructor(scope: Construct, id: string, props: Props) {
    super(scope, id);

    const httpApi = new HttpApi(this, "HttpApi", {
      apiName: "KindleRemindApi",
      createDefaultStage: false,
      disableExecuteApiEndpoint: false,
      defaultAuthorizer: props.authorizers.cognitoAuthorizer,
    });

    for (const lambdaConfig of LambdaConfigs.getEndpoints()) {
      const httpIntegration = new HttpLambdaIntegration(
        integrationName(lambdaConfig),
        props.lambdas.getByName(lambdaConfig.name)
      );

      httpApi.addRoutes({
        path: lambdaConfig.path,
        methods: [lambdaConfig.method!],
        integration: httpIntegration,
        authorizer: getAuthorizer(lambdaConfig, props.authorizers),
      });
    }

    new HttpStage(this, "Stage", {
      httpApi,
      stageName: "v1",
      autoDeploy: true,
    });
  }
}

function integrationName(config: LambdaConfig) {
  return `${config.name}HttpIntegration`;
}

function getAuthorizer(
  config: LambdaConfig,
  authorizers: Authorizers
): IHttpRouteAuthorizer | undefined {
  const authMap = {
    [Auth.ApiKey]: authorizers.apiKeyAuthorizer,
    [Auth.Cognito]: authorizers.cognitoAuthorizer,
  };

  return config.auth ? authMap[config.auth] : undefined;
}

interface Props {
  lambdas: Lambdas;
  authorizers: Authorizers;
}
