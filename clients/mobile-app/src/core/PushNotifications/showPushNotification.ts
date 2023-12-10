import {FirebaseMessagingTypes} from '@react-native-firebase/messaging';
import notifee from '@notifee/react-native';

import {Clipping} from '../Clipping/types';
import {createDefaultChannel} from './channel';
import {initialTheme} from '../../theme';

export async function showPushNotification(
  remoteMessage: FirebaseMessagingTypes.RemoteMessage,
) {
  try {
    const clipping: Clipping = JSON.parse(
      remoteMessage.data?.clipping as string,
    );

    await notifee.displayNotification({
      title: clipping.title,
      subtitle: 'Your book highlight',
      body: getBody(clipping),
      android: {
        channelId: await createDefaultChannel(),
        smallIcon: 'ic_notif_small_icon',
        color: initialTheme.darkColors?.primary,
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

const LEFT_QUOTATION_MARK = '&#8223;';
const RIGHT_QUOTATION_MARK = '&#8221;';

function getBody(clipping: Clipping) {
  // Single line to avoid unexpected white spaces.
  return `<p><span><b>${LEFT_QUOTATION_MARK}</b></span><i>${clipping.content}</i><b>${RIGHT_QUOTATION_MARK}</b></p>`;
}
