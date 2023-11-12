import {useCallback} from 'react';

import {useFetch} from '../../utils/useFetch';
import {useInitialPushToken, usePushTokenChanges} from '../../utils/pushToken';

export function useSavePushToken() {
  const postPushToken = usePostPushToken();
  useInitialPushToken(postPushToken);
  usePushTokenChanges(postPushToken);
}

function usePostPushToken() {
  const fetch = useFetch();

  return useCallback(
    async (pushToken: string, proto: string) => {
      await fetch('/push-token', {
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
