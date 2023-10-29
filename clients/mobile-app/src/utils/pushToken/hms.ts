import {useEffect} from 'react';
import {HmsPushInstanceId, HmsPushEvent} from '@hmscore/react-native-hms-push';

import {
  UseInitialPushToken,
  UsePushTokenChanges,
  PushTokenProto,
} from './types';

export const useInitialHmsPushToken: UseInitialPushToken = receivePushToken => {
  useEffect(() => {
    HmsPushInstanceId.getToken('')
      .then((rawResponse: Object) => {
        // Built-in type from HMS specifies the response as Object. Thus, it needs casting.
        const response = rawResponse as unknown as HmsPushTokenResponse;
        if (response?.result?.length) {
          receivePushToken(response.result, PushTokenProto.HMS);
        }
      })
      .catch(error => {
        console.error('Error receiving HMS Push Token', error);
      });
  }, [receivePushToken]);
};

// HMS Push has incorrect type for this function. Thus, it needs casting.
const onTokenReceived =
  HmsPushEvent.onTokenReceived as unknown as OnTokenReceived;

export const useHmsPushTokenChanges: UsePushTokenChanges = receivePushToken => {
  useEffect(() => {
    const subscription = onTokenReceived(response => {
      console.log('OnTokenReceived', response);
      if (response?.token?.length) {
        receivePushToken(response.token, PushTokenProto.HMS);
      }
    });

    return () => {
      subscription.remove();
    };
  }, [receivePushToken]);
};

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
