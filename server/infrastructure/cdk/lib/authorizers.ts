import { Construct } from "constructs";
import { UserPool, UserPoolClient } from "aws-cdk-lib/aws-cognito";

import { Lambdas } from "./lambdas";
import {
  HttpLambdaAuthorizer,
  HttpLambdaResponseType,
  HttpUserPoolAuthorizer,
} from "@aws-cdk/aws-apigatewayv2-authorizers-alpha";

export class Authorizers extends Construct {
  readonly apiKeyAuthorizer: HttpLambdaAuthorizer;
  readonly cognitoAuthorizer: HttpUserPoolAuthorizer;

  constructor(scope: Construct, id: string, props: Props) {
    super(scope, id);

    const apiKeyAuthorizerLambda = props.lambdas.getByName("ApiKeyAuthorizer");
    this.apiKeyAuthorizer = new HttpLambdaAuthorizer(
      "ApiKeyAuthorizer",
      apiKeyAuthorizerLambda,
      {
        authorizerName: "ApiKeyAuthorizer",
        responseTypes: [HttpLambdaResponseType.SIMPLE],
        identitySource: ["$request.header.Authorization"],
      }
    );

    this.cognitoAuthorizer = new HttpUserPoolAuthorizer(
      "UserPoolAuthorizer",
      props.userPool.instance,
      {
        userPoolClients: [props.userPool.appClient],
        identitySource: ["$request.header.Authorization"],
      }
    );
  }
}

interface Props {
  lambdas: Lambdas;
  userPool: {
    instance: UserPool;
    appClient: UserPoolClient;
  };
}
