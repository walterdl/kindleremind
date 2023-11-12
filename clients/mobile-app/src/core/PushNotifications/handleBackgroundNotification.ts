import messaging from '@react-native-firebase/messaging';

export function handleBackgroundNotification() {
  messaging().setBackgroundMessageHandler(async () => {
    // No need to manually show notification
    // as only presentational notifications are sent from server.
  });
}
