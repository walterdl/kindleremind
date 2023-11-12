import {useEffect} from 'react';
import messaging, {
  FirebaseMessagingTypes,
} from '@react-native-firebase/messaging';
import notifee from '@notifee/react-native';

import {createDefaultChannel} from './channel';

export function PushNotificationsPresenter() {
  useForegroundPushNotification();

  return null;
}

function useForegroundPushNotification() {
  useEffect(() => {
    const unsubscribe = messaging().onMessage(async remoteMessage => {
      await displayNotification(remoteMessage);
    });

    return unsubscribe;
  }, []);
}

async function displayNotification(
  remoteMessage: FirebaseMessagingTypes.RemoteMessage,
) {
  await notifee.displayNotification({
    title: remoteMessage.notification?.title,
    body: remoteMessage.notification?.body,
    android: {
      channelId: await createDefaultChannel(),
    },
  });
}
