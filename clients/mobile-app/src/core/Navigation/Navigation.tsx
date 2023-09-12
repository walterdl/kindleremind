import React from 'react';
import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';

import {useNavigationTheme} from '../../theme';
import {Authenticator} from '../Authenticator';
import {PrivateRoot} from './PrivateRoot';
import {RootScreenNames, RootStackParamList} from './types';

const Stack = createNativeStackNavigator<RootStackParamList>();

export function AppNavigation(): JSX.Element {
  const navigationTheme = useNavigationTheme();

  return (
    <NavigationContainer theme={navigationTheme}>
      <Stack.Navigator>
        <Stack.Screen name={RootScreenNames.Login} component={Authenticator} />
        <Stack.Screen
          name={RootScreenNames.PrivateRoot}
          component={PrivateRoot}
          options={{headerShown: false}}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
