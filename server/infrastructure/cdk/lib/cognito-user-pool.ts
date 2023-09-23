import { Construct } from "constructs";
import * as cdk from "aws-cdk-lib";
import * as cognito from "aws-cdk-lib/aws-cognito";

export class KrCognitoUserPool extends Construct {
  constructor(scope: Construct, id: string) {
    super(scope, id);

    const userPool = new cognito.UserPool(this, "CognitoUserPool", {
      userPoolName: "KindleRemindUserPool",
      accountRecovery: cognito.AccountRecovery.EMAIL_ONLY,
      selfSignUpEnabled: true,
      signInAliases: {
        username: true,
        email: true,
        phone: false,
        preferredUsername: false,
      },
      signInCaseSensitive: false,
      standardAttributes: {
        email: {
          required: true,
          mutable: true,
        },
      },
      userInvitation: {
        emailSubject: "Your invitation to join KindleRemind",
        emailBody:
          "Hello {username}, you have been invited to join KindleRemind. Your temporary password is {####}.",
      },
      userVerification: {
        emailSubject: "Verify your new account for KindleRemind",
        emailBody:
          "Hello {username}, Thanks for signing up to KindleRemind! Your verification code is {####}.",
        emailStyle: cognito.VerificationEmailStyle.CODE,
      },
    });

    userPool.addClient("KindleRemindMobileApp", {
      accessTokenValidity: cdk.Duration.hours(1),
      preventUserExistenceErrors: true,
      authFlows: {
        userSrp: true,
      },
      enableTokenRevocation: true,
      userPoolClientName: "KindleRemindMobileApp",
    });
  }
}
