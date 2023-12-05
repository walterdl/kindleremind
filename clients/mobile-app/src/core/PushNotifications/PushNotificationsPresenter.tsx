import {useCallback, useEffect} from 'react';
import messaging from '@react-native-firebase/messaging';
import notifee, {
  EventType,
  Event as NotificationEvent,
} from '@notifee/react-native';

import {showPushNotification} from './showPushNotification';
import {Event, addEventListener, removeEventListener} from '../../utils/events';
import {useNavigation, RootScreenNames} from '../Navigation';
import {Clipping} from '../Clipping';

export function PushNotificationsPresenter() {
  useInitialPushNotification();
  useForegroundPushNotification();
  useBackgroundPushNotification();

  return null;
}

function useForegroundPushNotification() {
  const goToClippingView = useGoToClippingView();

  useEffect(() => {
    // notifee.onForegroundEvent is used to detect when a notification is pressed.
    const unsubscribe = notifee.onForegroundEvent(event => {
      if (event.type === EventType.PRESS) {
        goToClippingView(
          event.detail.notification?.data as unknown as Clipping,
        );
      }
    });

    return unsubscribe;
  }, [goToClippingView]);

  useEffect(() => {
    const unsubscribe = messaging().onMessage(async remoteMessage => {
      await showPushNotification(remoteMessage);
    });

    return unsubscribe;
  }, []);
}

function useInitialPushNotification() {
  const goToClippingView = useGoToClippingView();

  useEffect(() => {
    notifee.getInitialNotification().then(initialNotification => {
      if (initialNotification) {
        goToClippingView(
          initialNotification?.notification.data as unknown as Clipping,
        );
      }
    });
  }, [goToClippingView]);
}

function useBackgroundPushNotification() {
  const goToClippingView = useGoToClippingView();

  useEffect(() => {
    function handleBackgroundPushNotification(
      notificationEvent: NotificationEvent,
    ) {
      goToClippingView(
        notificationEvent.detail.notification?.data as unknown as Clipping,
      );
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

function useGoToClippingView() {
  const navigate = useNavigation();

  return useCallback(
    (clipping: Clipping) => {
      navigate.navigate(RootScreenNames.ClippingView, {
        clipping,
      });
    },
    [navigate],
  );
}
