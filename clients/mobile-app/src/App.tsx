/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 */

import React from 'react';
import {ThemeProvider} from '@rneui/themed';
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

function AppNavigation(): JSX.Element {
  const navigationTheme = useNavigationTheme();

  return (
    <NavigationContainer theme={navigationTheme}>
      <Stack.Navigator>
        <Stack.Screen name={ScreenNames.Login} component={Authenticator} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
