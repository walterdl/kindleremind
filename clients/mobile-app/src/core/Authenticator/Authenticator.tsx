import React from 'react';
import {Amplify} from 'aws-amplify';
import {
  Authenticator,
  ThemeProvider as AuthThemeProvider,
} from '@aws-amplify/ui-react-native';
import {DefaultSignUpProps} from '@aws-amplify/ui-react-native/dist/Authenticator/Defaults/types';

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
            SignUp,
          }}>
          {children}
        </Authenticator>
      </Authenticator.Provider>
    </AuthThemeProvider>
  );
}

function SignUp(props: DefaultSignUpProps) {
  return <Authenticator.SignUp {...props} fields={signUpFields} />;
}

interface Props {
  children: React.ReactNode;
}
