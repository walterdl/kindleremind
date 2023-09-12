import {useCallback} from 'react';
import {useNavigation} from '@react-navigation/native';

import {PrivateRootScreenNavigationProp, RootScreenNames} from '../Navigation';
import {useDeleteApiKey} from '../apiKeyStore';

export function useLogout() {
  const navigation = useNavigation<PrivateRootScreenNavigationProp>();
  const deleteApiKey = useDeleteApiKey();

  return useCallback(async () => {
    await deleteApiKey();
    navigation.reset({
      index: 0,
      routes: [{name: RootScreenNames.Login}],
    });
  }, [deleteApiKey, navigation]);
}
