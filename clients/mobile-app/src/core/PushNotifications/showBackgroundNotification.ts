import messaging from '@react-native-firebase/messaging';
import notifee, {EventType} from '@notifee/react-native';

import {Event, emitEvent} from '../../utils/events';
import {showPushNotification} from './showPushNotification';

export function showBackgroundPushNotification() {
  notifee.onBackgroundEvent(async notificationEvent => {
    if (notificationEvent.type === EventType.PRESS) {
      // User tapped on the notification when app was in background.
      emitEvent(Event.ON_BACKGROUND_PUSH_NOTIFICATION, notificationEvent);
    }
  });

  messaging().setBackgroundMessageHandler(async remoteMessage => {
    await showPushNotification(remoteMessage);
  });
}
