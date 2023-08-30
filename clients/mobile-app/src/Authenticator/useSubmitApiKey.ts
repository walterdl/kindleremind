import {useCallback} from 'react';
import Config from 'react-native-config';

export function useSubmitApiKey() {
  return useCallback(async (apiKey: string) => {
    const response = await fetch(Config.API_URL + '/status', {
      headers: {
        Authorization: apiKey,
      },
    });

    if (response.ok) {
      const result: Partial<{date: string}> = await response.json();
      // Status endpoint returns the current date if the API key is valid
      return !!result?.date;
    }

    if (response.status === 403) {
      return false;
    }

    throw new Error('Unexpected response: ' + response.statusText);
  }, []);
}
