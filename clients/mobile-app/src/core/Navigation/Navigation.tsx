import React from 'react';
import {makeStyles, Button} from '@rneui/themed';
import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';
import {useAuthenticator} from '@aws-amplify/ui-react-native';

import {useNavigationTheme} from '../../theme';
import {RootScreenNames, RootStackParamList} from './types';
import {Home} from '../Home';
import {useSavePushToken} from './useSavePushToken';

const Stack = createNativeStackNavigator<RootStackParamList>();
const useStyles = makeStyles(theme => ({
  sceneContent: {
    padding: theme.spacing.md,
  },
}));

export function AppNavigation(): JSX.Element {
  const navigationTheme = useNavigationTheme();
  const styles = useStyles();

  useSavePushToken();

  return (
    <NavigationContainer theme={navigationTheme}>
      <Stack.Navigator
        initialRouteName={RootScreenNames.Clippings}
        screenOptions={{
          contentStyle: styles.sceneContent,
          headerBackVisible: false,
          headerRight: HeaderRight,
        }}>
        <Stack.Screen name={RootScreenNames.Clippings} component={Home} />
      </Stack.Navigator>
    </NavigationContainer>
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
