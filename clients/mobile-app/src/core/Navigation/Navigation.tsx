import React from 'react';
import {makeStyles} from '@rneui/themed';
import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';

import {useNavigationTheme} from '../../theme';
import {Authenticator} from '../Authenticator';
import {Home as HomeScreen} from '../Home';
import {ScreenNames, RootStackParamList} from './types';

const Stack = createNativeStackNavigator<RootStackParamList>();

const useStyles = makeStyles(theme => ({
  sceneContent: {
    padding: theme.spacing.md,
  },
}));

export function AppNavigation(): JSX.Element {
  const navigationTheme = useNavigationTheme();
  const styles = useStyles();

  return (
    <NavigationContainer theme={navigationTheme}>
      <Stack.Navigator screenOptions={{contentStyle: styles.sceneContent}}>
        <Stack.Screen name={ScreenNames.Login} component={Authenticator} />
        <Stack.Screen name={ScreenNames.Home} component={HomeScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
