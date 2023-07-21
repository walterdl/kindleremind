import * as cdk from "aws-cdk-lib";
import * as ssm from "aws-cdk-lib/aws-ssm";
import * as iam from "aws-cdk-lib/aws-iam";
import { Construct } from "constructs";

export class AccessesStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const mongoAtlasAccountId =
      ssm.StringParameter.fromStringParameterAttributes(
        this,
        "MongoAtlasAccountId",
        {
          parameterName: "/kindleremind/mongo-atlas/account-id",
        }
      ).stringValue;
    const mongoAtlasExternalId =
      ssm.StringParameter.fromStringParameterAttributes(
        this,
        "MongoAtlasExternalId",
        {
          parameterName: "/kindleremind/mongo-atlas/external-id",
        }
      ).stringValue;

    new iam.Role(this, "AtlasAccessRole", {
      assumedBy: new iam.AccountPrincipal(mongoAtlasAccountId),
      externalIds: [mongoAtlasExternalId],
    });
  }
}
