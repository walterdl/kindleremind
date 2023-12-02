import {useEffect} from 'react';
import messaging from '@react-native-firebase/messaging';
import notifee, {
  EventType,
  Event as NotificationEvent,
} from '@notifee/react-native';

import {showPushNotification} from './showPushNotification';
import {Event, addEventListener, removeEventListener} from '../../utils/events';

export function PushNotificationsPresenter() {
  useInitialPushNotification();
  useForegroundPushNotification();
  useBackgroundPushNotification();

  return null;
}

function useForegroundPushNotification() {
  useEffect(() => {
    // notifee.onForegroundEvent is used to detect when a notification is pressed.
    const unsubscribe = notifee.onForegroundEvent(event => {
      if (event.type === EventType.PRESS) {
        // TODO: Go to Clipping view.
      }
    });

    return unsubscribe;
  }, []);

  useEffect(() => {
    const unsubscribe = messaging().onMessage(async remoteMessage => {
      await showPushNotification(remoteMessage);
    });

    return unsubscribe;
  }, []);
}

function useInitialPushNotification() {
  useEffect(() => {
    notifee.getInitialNotification().then(_initialNotification => {
      // TODO: go to Clipping view.
    });
  }, []);
}

function useBackgroundPushNotification() {
  useEffect(() => {
    function handleBackgroundPushNotification(
      _notificationEvent: NotificationEvent,
    ) {
      // TODO: go to Clipping view.
    }

    addEventListener(
      Event.ON_BACKGROUND_PUSH_NOTIFICATION,
      handleBackgroundPushNotification,
    );

    return () => {
      removeEventListener(
        Event.ON_BACKGROUND_PUSH_NOTIFICATION,
        handleBackgroundPushNotification,
      );
    };
  });
}
