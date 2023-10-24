import {useCallback, useEffect} from 'react';
import {HmsPushInstanceId, HmsPushEvent} from '@hmscore/react-native-hms-push';
import Config from 'react-native-config';
import {useFetch} from '../../utils/useFetch';

const POST_TOKEN_URL = Config.API_URL + '/push-token';

export function useSavePushToken() {
  const postPushToken = usePostPushToken();
  useInitialPushToken(postPushToken);
  useSubscribeToPushTokenChange(postPushToken);
}

function usePostPushToken() {
  const fetch = useFetch();

  return useCallback<ReceiveToken>(
    async token => {
      await fetch(POST_TOKEN_URL, {
        method: 'POST',
        body: JSON.stringify({pushToken: token}),
        headers: {
          'Content-Type': 'application/json',
        },
      });
    },
    [fetch],
  );
}

function useInitialPushToken(receiveToken: ReceiveToken) {
  useEffect(() => {
    HmsPushInstanceId.getToken('')
      .then((rawResponse: Object) => {
        // Built-in type from HMS specifies the response as Object. Thus, it needs casting.
        const response = rawResponse as unknown as HmsPushTokenResponse;
        if (response?.result?.length) {
          receiveToken(response.result);
        }
      })
      .catch(error => {
        console.error('Error receiving HMS Push Token', error);
      });
  }, [receiveToken]);
}

// HMS Push has incorrect type for this function. Thus, it needs casting.
const onTokenReceived =
  HmsPushEvent.onTokenReceived as unknown as OnTokenReceived;

function useSubscribeToPushTokenChange(receiveToken: ReceiveToken) {
  useEffect(() => {
    const subscription = onTokenReceived(response => {
      console.log('OnTokenReceived', response);
      if (response?.token?.length) {
        receiveToken(response.token);
      }
    });

    return () => {
      subscription.remove();
    };
  }, [receiveToken]);
}

type ReceiveToken = (token: string) => Promise<void>;

interface HmsPushTokenResponse {
  result?: string;
  resultCode: string;
}

type OnTokenReceived = (
  callback: (response?: OnTokenReceivedResponse) => void,
) => OnTokenReceivedSubscription;

interface OnTokenReceivedResponse {
  token?: string;
}

type OnTokenReceivedSubscription = {
  remove: () => void;
};
