import {useCallback} from 'react';
import secureStore from 'react-native-sensitive-info';

const API_KEY_NAME = 'kindleremind_api_key';

export function useSaveApiKey() {
  return useCallback(async (value: string) => {
    await secureStore.setItem(API_KEY_NAME, value, {});
  }, []);
}

export function useGetApiKey() {
  return useCallback(async () => {
    return secureStore.getItem(API_KEY_NAME, {});
  }, []);
}

export function useDeleteApiKey() {
  return useCallback(async () => {
    return secureStore.deleteItem(API_KEY_NAME, {});
  }, []);
}
