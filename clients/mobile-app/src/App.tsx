import React from 'react';
import {ThemeProvider, makeStyles} from '@rneui/themed';
import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';

import {initialTheme, useNavigationTheme} from './theme';
import {Authenticator} from './Authenticator';

const Stack = createNativeStackNavigator();

enum ScreenNames {
  Login = 'Login',
}

function App(): JSX.Element {
  return (
    <ThemeProvider theme={initialTheme}>
      <AppNavigation />
    </ThemeProvider>
  );
}

const useStyles = makeStyles(theme => ({
  sceneContent: {
    padding: theme.spacing.md,
  },
}));

function AppNavigation(): JSX.Element {
  const navigationTheme = useNavigationTheme();
  const styles = useStyles();

  return (
    <NavigationContainer theme={navigationTheme}>
      <Stack.Navigator screenOptions={{contentStyle: styles.sceneContent}}>
        <Stack.Screen name={ScreenNames.Login} component={Authenticator} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
