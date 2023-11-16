import React from 'react';
import {View} from 'react-native';
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
import {Schedules} from '../Schedules';

const Stack = createNativeStackNavigator<RootStackParamList>();
const useStyles = makeStyles(theme => ({
  container: {
    backgroundColor: theme.colors.background,
    flex: 1,
  },
  sceneContent: {
    paddingHorizontal: theme.spacing.md,
  },
}));

export function AppNavigation(): JSX.Element {
  const navigationTheme = useNavigationTheme();
  const styles = useStyles();

  useSavePushToken();

  return (
    <View style={styles.container}>
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
          <Stack.Screen
            name={RootScreenNames.Schedules}
            component={Schedules}
            options={{title: 'Schedules'}}
          />
        </Stack.Navigator>
      </NavigationContainer>
    </View>
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
