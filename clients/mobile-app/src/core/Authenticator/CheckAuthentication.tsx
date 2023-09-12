import React, {useEffect} from 'react';
import {View, ActivityIndicator} from 'react-native';
import {Text} from '@rneui/themed';

import {useGetApiKey} from '../apiKeyStore';
import {useSubmitApiKey} from './useSubmitApiKey';
import {NativeStackScreenProps} from '@react-navigation/native-stack';
import {RootScreenNames, RootStackParamList} from '../Navigation';

type Props = NativeStackScreenProps<
  RootStackParamList,
  RootScreenNames.CheckLogin
>;

export function CheckAuthentication(props: Props) {
  const getApiKey = useGetApiKey();
  const submitApiKey = useSubmitApiKey();

  useEffect(() => {
    async function execute() {
      let isValid = false;

      try {
        const apiKey = await getApiKey();
        if (apiKey) {
          isValid = await submitApiKey(apiKey);
        }
      } catch {
        // Do nothing. If an error occurs, the user will be redirected to the login screen.
      }

      if (isValid) {
        return props.navigation.replace(RootScreenNames.PrivateRoot);
      }

      return props.navigation.replace(RootScreenNames.Login);
    }

    execute();
  }, [getApiKey, props.navigation, submitApiKey]);

  return (
    <View>
      <Text>Checking session</Text>
      <ActivityIndicator />
    </View>
  );
}
