import { Construct } from "constructs";
import { HttpLambdaIntegration } from "@aws-cdk/aws-apigatewayv2-integrations-alpha";
import { ARecord, RecordTarget } from "aws-cdk-lib/aws-route53";
import { ApiGatewayv2DomainProperties } from "aws-cdk-lib/aws-route53-targets";
import {
  HttpApi,
  IHttpRouteAuthorizer,
  HttpStage,
  DomainName,
} from "@aws-cdk/aws-apigatewayv2-alpha";

import { LambdaConfigs, LambdaConfig, Auth } from "./lambdas-config";
import { Lambdas } from "./lambdas";
import { Authorizers } from "./authorizers";
import { KrDomainName } from "./domain-name";

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

    const domainNameInstance = new DomainName(this, "ApiDomainName", {
      domainName: props.domainName.getDomainName(props.domainName.apiSubdomain),
      certificate: props.domainName.apiCertificate,
    });
    new HttpStage(this, "Stage", {
      httpApi,
      stageName: "v1",
      autoDeploy: true,
      domainMapping: {
        domainName: domainNameInstance,
      },
    });

    new ARecord(scope, "ApiRoute53AliasRecord", {
      recordName: props.domainName.apiSubdomain,
      zone: props.domainName.hostedZone,
      target: RecordTarget.fromAlias(
        new ApiGatewayv2DomainProperties(
          domainNameInstance.regionalDomainName,
          domainNameInstance.regionalHostedZoneId
        )
      ),
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
  domainName: KrDomainName;
}
