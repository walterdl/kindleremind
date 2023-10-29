import {useEffect} from 'react';
import messaging from '@react-native-firebase/messaging';

import {
  UseInitialPushToken,
  UsePushTokenChanges,
  PushTokenProto,
} from './types';

export const useInitialFcmPushToken: UseInitialPushToken = receivePushToken => {
  useEffect(() => {
    messaging()
      .getToken()
      .then(token => {
        receivePushToken(token, PushTokenProto.FCM);
      });
  }, [receivePushToken]);
};

export const useFcmPushTokenChanges: UsePushTokenChanges = receivePushToken => {
  useEffect(() => {
    const unsubscribe = messaging().onTokenRefresh(token => {
      receivePushToken(token, PushTokenProto.HMS);
    });

    return unsubscribe;
  }, [receivePushToken]);
};
