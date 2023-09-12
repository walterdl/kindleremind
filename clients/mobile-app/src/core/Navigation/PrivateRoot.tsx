import React from 'react';
import {makeStyles, Button} from '@rneui/themed';
import {useNavigation} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';

import {
  PrivateRootStackParamList,
  PrivateRootScreenNames,
  PrivateRootScreenNavigationProp,
} from './types';
import {Home} from '../Home';
import {useDeleteApiKey} from '../apiKeyStore';

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
  const navigation = useNavigation<PrivateRootScreenNavigationProp>();
  const deleteApiKey = useDeleteApiKey();
  const logout = async () => {
    await deleteApiKey();
    navigation.popToTop();
  };

  return (
    <Button type="clear" onPress={logout}>
      Logout
    </Button>
  );
}
