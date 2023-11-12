import React from 'react';
import {ThemeProvider} from '@rneui/themed';
import {AlertNotificationRoot} from 'react-native-alert-notification';

import {initialTheme} from './theme';
import {AppAuthenticator} from './core/Authenticator';
import {AppNavigation} from './core/Navigation';
import {createDefaultChannel} from './core/pushNotifications';

createDefaultChannel();

function App(): JSX.Element {
  return (
    <ThemeProvider theme={initialTheme}>
      <AppAuthenticator>
        <AlertNotificationRoot theme="dark">
          <AppNavigation />
        </AlertNotificationRoot>
      </AppAuthenticator>
    </ThemeProvider>
  );
}

export default App;
