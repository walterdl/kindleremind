import {useCallback} from 'react';
import {Auth} from 'aws-amplify';
import {useAuthenticator} from '@aws-amplify/ui-react-native';

export function useFetch() {
  const {signOut} = useAuthenticator();

  return useCallback(
    async (url: string, options: RequestInit = {}) => {
      const token = await getSessionToken();
      if (!token) {
        signOut();
        throw new Error('No session token');
      }

      addAuthorization(options, token);
      return fetch(url, options);
    },
    [signOut],
  );
}

async function getSessionToken(): Promise<string | null> {
  try {
    const session = await Auth.currentSession();

    // ID Token used instead of Access Token to get user information.
    // This way, server can associate submitted data with friendly user data.
    return session.getIdToken().getJwtToken();
  } catch {
    return null;
  }
}

function addAuthorization(options: RequestInit, token: string) {
  if (!options.headers) {
    options.headers = {};
  }

  (options.headers as {[key: string]: string}).Authorization = token;
}
