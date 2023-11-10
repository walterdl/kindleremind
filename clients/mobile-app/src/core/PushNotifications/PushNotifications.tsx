import React from 'react';
import {View, Linking} from 'react-native';
import {Text, Button} from '@rneui/themed';

import {usePermissionStatus, PermissionStatus} from './usePermissionStatus';

export function PushNotifications() {
  const {permissionStatus, requestPermission} = usePermissionStatus();

  const notGranted = (
    ['denied', 'never_ask_again'] as PermissionStatus[]
  ).includes(permissionStatus);

  return (
    <View>
      <Text>
        {permissionStatus === 'checking' &&
          'Checking push notification permissions'}
        {permissionStatus === 'granted' &&
          "You'll receive push notifications about your Kindle clippings"}
        {notGranted &&
          'Push notifications disabled. You will not receive reminders until you grant permission.'}
      </Text>
      {notGranted && (
        <Button
          title="Grant notification permissions"
          onPress={() => {
            if (permissionStatus === 'denied') {
              return requestPermission();
            }

            // Its 'never_ask_again'. Only the settings can fix this.
            Linking.openSettings();
          }}
        />
      )}
    </View>
  );
}
