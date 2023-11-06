import {useFcmPushTokenChanges, useInitialFcmPushToken} from './fcm';
import {UseInitialPushToken, UsePushTokenChanges} from './types';

export const usePushTokenChanges: UsePushTokenChanges = receivePushToken =>
  useFcmPushTokenChanges(receivePushToken);
export const useInitialPushToken: UseInitialPushToken = receivePushToken =>
  useInitialFcmPushToken(receivePushToken);
