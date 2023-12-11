import React from 'react';
import {Image} from 'react-native';
import {Amplify} from 'aws-amplify';
import {
  Authenticator,
  ThemeProvider as AuthThemeProvider,
} from '@aws-amplify/ui-react-native';
import {DefaultSignUpProps} from '@aws-amplify/ui-react-native/dist/Authenticator/Defaults/types';
import {makeStyles} from '@rneui/themed';

import {awsExports} from './awsExports';
import {theme} from './theme';
import {signUpFields} from './signUpFields';
import {View} from 'react-native';

Amplify.configure(awsExports);

export function AppAuthenticator({children}: Props) {
  return (
    <AuthThemeProvider theme={theme} colorMode={'dark'}>
      <Authenticator.Provider>
        <Authenticator
          loginMechanisms={['email']}
          signUpAttributes={['email', 'given_name']}
          Header={Header}
          components={{
            SignUp,
          }}>
          {children}
        </Authenticator>
      </Authenticator.Provider>
    </AuthThemeProvider>
  );
}

const headerStyles = makeStyles(() => ({
  container: {
    width: '100%',
    height: 125,
  },
  img: {
    width: '100%',
    flex: 1,
    resizeMode: 'contain',
  },
}));

function Header() {
  const styles = headerStyles();
  return (
    <View style={styles.container}>
      <Image source={require('./logo.png')} style={styles.img} />
    </View>
  );
}

function SignUp(props: DefaultSignUpProps) {
  return <Authenticator.SignUp {...props} fields={signUpFields} />;
}

interface Props {
  children: React.ReactNode;
}
