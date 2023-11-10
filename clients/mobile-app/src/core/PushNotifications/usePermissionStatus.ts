import {useCallback, useEffect, useRef, useState} from 'react';
import {
  PermissionsAndroid,
  PermissionStatus as NativePermissionStatus,
} from 'react-native';

export function usePermissionStatus() {
  const [permissionStatus, setPermissionStatus] =
    useState<PermissionStatus>('checking');

  const requestPermission = useRequestPermission(setPermissionStatus);

  useInitializePermission(requestPermission);

  return {permissionStatus, requestPermission};
}

function useRequestPermission(
  setPermissionStatus: SetPermissionStatus,
): RequestPermission {
  const fetchNativePermission = useFetchNativePermission();

  return useCallback(async () => {
    const isGranted = await PermissionsAndroid.check(
      PermissionsAndroid.PERMISSIONS.POST_NOTIFICATIONS,
    );

    if (isGranted) {
      setPermissionStatus('granted');
      return;
    }

    const result = await fetchNativePermission();
    setPermissionStatus(result);
  }, [fetchNativePermission, setPermissionStatus]);
}

function useInitializePermission(requestPermission: RequestPermission) {
  const executed = useRef(false);

  useEffect(() => {
    async function execute() {
      if (executed.current) {
        return;
      }

      executed.current = true;
      requestPermission();
    }

    execute();
  }, [requestPermission]);
}

function useFetchNativePermission() {
  return useCallback(async (): Promise<PermissionStatus> => {
    try {
      const result = await PermissionsAndroid.request(
        PermissionsAndroid.PERMISSIONS.POST_NOTIFICATIONS,
        {
          title: 'Kindleremind Push Notification Permission',
          message:
            'Kindleremind needs permission to show push notifications so you can receive reminders.',
          buttonNeutral: 'Ask Me Later',
          buttonNegative: 'Cancel',
          buttonPositive: 'OK',
        },
      );

      return result;
    } catch (err) {
      console.warn(err);
      return 'error';
    }
  }, []);
}

export type PermissionStatus = NativePermissionStatus | 'error' | 'checking';
type SetPermissionStatus = (status: PermissionStatus) => void;
type RequestPermission = () => Promise<void>;
