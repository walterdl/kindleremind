import {utils} from '@react-native-firebase/app';

import {useHmsPushTokenChanges, useInitialHmsPushToken} from './hms';
import {useFcmPushTokenChanges, useInitialFcmPushToken} from './fcm';
import {UseInitialPushToken, UsePushTokenChanges} from './types';

const {isAvailable: hasGooglePlayServices} = utils().playServicesAvailability;

let _usePushTokenChanges: UsePushTokenChanges;
let _useInitialPushToken: UseInitialPushToken;

if (hasGooglePlayServices) {
  _usePushTokenChanges = useFcmPushTokenChanges;
  _useInitialPushToken = useInitialFcmPushToken;
} else {
  _usePushTokenChanges = useHmsPushTokenChanges;
  _useInitialPushToken = useInitialHmsPushToken;
}

export const usePushTokenChanges: UsePushTokenChanges = receivePushToken =>
  _usePushTokenChanges(receivePushToken);
export const useInitialPushToken: UseInitialPushToken = receivePushToken =>
  _useInitialPushToken(receivePushToken);
