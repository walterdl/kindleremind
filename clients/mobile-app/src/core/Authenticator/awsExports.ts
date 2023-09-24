import Config from 'react-native-config';

export const awsExports = {
  Auth: {
    region: Config.USER_POOL_REGION,
    userPoolId: Config.USER_POOL_ID,
    userPoolWebClientId: Config.USER_POOL_WEB_CLIENT_ID,
    mandatorySignIn: true,
    authenticationFlowType: 'USER_SRP_AUTH',
  },
};
