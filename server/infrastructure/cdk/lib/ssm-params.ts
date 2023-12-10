import { Construct } from "constructs";
import * as ssm from "aws-cdk-lib/aws-ssm";
import { IGrantable } from "aws-cdk-lib/aws-iam";

export const SSM_PARAM_NAMES = {
  MONGODB_URI_SSM_NAME: "/kindleremind/mongo-atlas/connection-uri",
  API_KEY_SSM_NAME: "/kindleremind/api-key",
  FIREBASE_SERVICE_ACCOUNT_PRIVATE_KEY_SSM_NAME:
    "/kindleremind/firebase/service-account/private-key",
};

export class SsmParams extends Construct {
  readonly params: Params;

  constructor(scope: Construct, id: string) {
    super(scope, id);

    this.params = {} as Params;
    for (const varName in SSM_PARAM_NAMES) {
      if (Object.prototype.hasOwnProperty.call(SSM_PARAM_NAMES, varName)) {
        const paramName =
          SSM_PARAM_NAMES[varName as keyof typeof SSM_PARAM_NAMES];
        const param = ssm.StringParameter.fromSecureStringParameterAttributes(
          this,
          varName,
          {
            parameterName: paramName,
          }
        );
        this.params[varName as VarNames] = param;
      }
    }
  }

  grantRead(grantees: IGrantable[]): void {
    for (const x of grantees) {
      for (const param of Object.values(this.params)) {
        param.grantRead(x);
      }
    }
  }
}

export type VarNames = keyof typeof SSM_PARAM_NAMES;
export type Params = { [key in VarNames]: ssm.IStringParameter };
