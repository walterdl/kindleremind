import React from 'react';
import {ThemeProvider} from '@rneui/themed';

import {initialTheme} from './theme';
import {AppAuthenticator} from './core/Authenticator';
import {AppNavigation} from './core/Navigation';

function App(): JSX.Element {
  return (
    <ThemeProvider theme={initialTheme}>
      <AppAuthenticator>
        <AppNavigation />
      </AppAuthenticator>
    </ThemeProvider>
  );
}

export default App;
