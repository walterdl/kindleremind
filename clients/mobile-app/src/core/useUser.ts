import {useAuthenticator} from '@aws-amplify/ui-react-native';
import {useMemo} from 'react';

export function useUser() {
  const {user} = useAuthenticator();

  return useMemo<User>(
    () => ({
      firstName: user.attributes?.given_name || '',
    }),
    [user.attributes?.given_name],
  );
}

interface User {
  firstName: string;
}
