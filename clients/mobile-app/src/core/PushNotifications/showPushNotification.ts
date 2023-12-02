import {FirebaseMessagingTypes} from '@react-native-firebase/messaging';
import notifee from '@notifee/react-native';

import {Clipping} from '../Clippings/types';
import {createDefaultChannel} from './channel';

export async function showPushNotification(
  remoteMessage: FirebaseMessagingTypes.RemoteMessage,
) {
  try {
    const clipping: Clipping = JSON.parse(
      remoteMessage.data?.clipping as string,
    );
    await notifee.displayNotification({
      title: clipping.title,
      body: clipping.content,
      android: {
        channelId: await createDefaultChannel(),
        pressAction: {
          id: clipping.id,
          launchActivity: 'default',
        },
      },
      data: clipping as unknown as Record<string, string>,
    });
  } catch (error) {
    console.error('Error showing push notificatin', error);
  }
}
