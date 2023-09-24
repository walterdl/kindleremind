import React from 'react';
import {Amplify} from 'aws-amplify';
import {
  Authenticator,
  ThemeProvider as AuthThemeProvider,
} from '@aws-amplify/ui-react-native';

import {awsExports} from './awsExports';
import {theme} from './theme';
import {signUpFields} from './signUpFields';

Amplify.configure(awsExports);

export function AppAuthenticator({children}: Props) {
  return (
    <AuthThemeProvider theme={theme} colorMode={'dark'}>
      <Authenticator.Provider>
        <Authenticator
          loginMechanisms={['email']}
          signUpAttributes={['email', 'given_name']}
          components={{
            SignUp: props => {
              return <Authenticator.SignUp {...props} fields={signUpFields} />;
            },
          }}>
          {children}
        </Authenticator>
      </Authenticator.Provider>
    </AuthThemeProvider>
  );
}

interface Props {
  children: React.ReactNode;
}
