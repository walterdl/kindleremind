import React from 'react';
import {ThemeProvider} from '@rneui/themed';

import {initialTheme} from './theme';
import {AppNavigation} from './core/Navigation';

function App(): JSX.Element {
  return (
    <ThemeProvider theme={initialTheme}>
      <AppNavigation />
    </ThemeProvider>
  );
}

export default App;
