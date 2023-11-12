import notifee, {AndroidVisibility} from '@notifee/react-native';

export async function createDefaultChannel() {
  const channelId = await notifee.createChannel({
    id: 'default',
    name: 'Default reminders',
    vibration: true,
    sound: 'default',
    visibility: AndroidVisibility.PUBLIC,
  });

  return channelId;
}
