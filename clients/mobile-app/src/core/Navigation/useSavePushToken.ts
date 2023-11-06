import {useCallback} from 'react';
import Config from 'react-native-config';

import {useFetch} from '../../utils/useFetch';
import {useInitialPushToken, usePushTokenChanges} from '../../utils/pushToken';

const POST_TOKEN_URL = Config.API_URL + '/push-token';

export function useSavePushToken() {
  const postPushToken = usePostPushToken();
  useInitialPushToken(postPushToken);
  usePushTokenChanges(postPushToken);
}

function usePostPushToken() {
  const fetch = useFetch();

  return useCallback(
    async (pushToken: string, proto: string) => {
      await fetch(POST_TOKEN_URL, {
        method: 'POST',
        body: JSON.stringify({pushToken, proto}),
        headers: {
          'Content-Type': 'application/json',
        },
      });
    },
    [fetch],
  );
}
