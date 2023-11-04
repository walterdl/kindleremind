import {useCallback} from 'react';
import {Auth} from 'aws-amplify';
import {useAuthenticator} from '@aws-amplify/ui-react-native';
import Config from 'react-native-config';

const defaultOptions: UseFetchOptions = {
  withApiBaseUrl: true,
};

export function useFetch(options: UseFetchOptions = defaultOptions) {
  const {signOut} = useAuthenticator();

  return useCallback(
    async (url: string, fetchOptions: FetchOptions = {}) => {
      const token = await getSessionToken();
      if (!token) {
        signOut();
        throw new Error('No session token');
      }

      addAuthorization(fetchOptions, token);

      if (options.withApiBaseUrl) {
        url = Config.API_URL + url + queryParams(fetchOptions);
      }

      return fetch(url, fetchOptions);
    },
    [options.withApiBaseUrl, signOut],
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

function queryParams(fetchOptions: FetchOptions) {
  if (fetchOptions.queryParams) {
    const result = new URLSearchParams(fetchOptions.queryParams);
    return '?' + result.toString();
  }

  return '';
}

export interface UseFetchOptions {
  /**
   * @default true
   */
  withApiBaseUrl?: boolean;
}

export type Fetch = (
  url: string,
  fetchOptions?: FetchOptions,
) => Promise<Response>;

export interface FetchOptions extends RequestInit {
  queryParams?: Record<string, string>;
}

function addAuthorization(options: RequestInit, token: string) {
  if (!options.headers) {
    options.headers = {};
  }

  const headers = options.headers as {[key: string]: string};
  headers.Authorization = token;
  headers['Content-Type'] = 'application/json';
}
