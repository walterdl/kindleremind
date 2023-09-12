import React from 'react';
import {makeStyles, Button} from '@rneui/themed';
import {createNativeStackNavigator} from '@react-navigation/native-stack';

import {PrivateRootStackParamList, PrivateRootScreenNames} from './types';
import {Home} from '../Home';
import {useLogout} from '../Authenticator';

const Stack = createNativeStackNavigator<PrivateRootStackParamList>();

const useStyles = makeStyles(theme => ({
  sceneContent: {
    padding: theme.spacing.md,
  },
}));

export function PrivateRoot() {
  const styles = useStyles();

  return (
    <Stack.Navigator
      screenOptions={{
        contentStyle: styles.sceneContent,
        headerBackVisible: false,
        headerRight: HeaderRight,
      }}>
      <Stack.Screen name={PrivateRootScreenNames.Clippings} component={Home} />
    </Stack.Navigator>
  );
}

function HeaderRight() {
  const logout = useLogout();

  return (
    <Button type="clear" onPress={logout}>
      Logout
    </Button>
  );
}
