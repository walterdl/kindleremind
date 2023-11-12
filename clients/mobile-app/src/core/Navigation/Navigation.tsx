import React from 'react';
import {makeStyles, Button} from '@rneui/themed';
import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';
import {useAuthenticator} from '@aws-amplify/ui-react-native';

import {useNavigationTheme} from '../../theme';
import {RootScreenNames, RootStackParamList} from './types';
import {Home} from '../Home';
import {ApiKeysView} from '../ApiKeys';
import {useSavePushToken} from './useSavePushToken';
import {PushNotificationsPresenter} from '../pushNotifications';

const Stack = createNativeStackNavigator<RootStackParamList>();
const useStyles = makeStyles(theme => ({
  sceneContent: {
    padding: theme.spacing.xl,
  },
}));

export function AppNavigation(): JSX.Element {
  const navigationTheme = useNavigationTheme();
  const styles = useStyles();

  useSavePushToken();

  return (
    <>
      <PushNotificationsPresenter />
      <NavigationContainer theme={navigationTheme}>
        <Stack.Navigator
          initialRouteName={RootScreenNames.Clippings}
          screenOptions={{
            contentStyle: styles.sceneContent,
            headerRight: HeaderRight,
          }}>
          <Stack.Screen
            name={RootScreenNames.Clippings}
            component={Home}
            options={{title: 'Kindleremind'}}
          />
          <Stack.Screen
            name={RootScreenNames.ApiKeys}
            component={ApiKeysView}
            options={{title: 'API Keys'}}
          />
        </Stack.Navigator>
      </NavigationContainer>
    </>
  );
}

function HeaderRight() {
  const {signOut} = useAuthenticator();

  return (
    <Button type="clear" onPress={signOut}>
      Sign out
    </Button>
  );
}
