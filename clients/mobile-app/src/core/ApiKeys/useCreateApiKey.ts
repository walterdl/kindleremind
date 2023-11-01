import {useCallback, useState} from 'react';
import {useFetch} from '../../utils/useFetch';
import type {ApiKey} from './types';
import {useApiKeysState} from './apiKeysState';

export function useCreateApiKey() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);
  const post = usePost();
  const addApiKeyToState = useAddApiKeyToState();

  const createApiKey = useCallback(
    async (name: string) => {
      try {
        setLoading(true);
        setError(false);
        const newApiKey = await post(name);
        addApiKeyToState(newApiKey);
      } catch {
        setError(true);
      } finally {
        setLoading(false);
      }
    },
    [addApiKeyToState, post],
  );

  const cleanError = useCallback(() => {
    setError(false);
  }, []);

  return {createApiKey, loading, error, cleanError};
}

function usePost() {
  const fetch = useFetch();

  return useCallback(
    async (name: string) => {
      const response = await fetch('/api-keys', {
        body: JSON.stringify({name}),
        method: 'POST',
      });

      if (!response.ok) {
        throw new Error();
      }

      return response.json() as Promise<ApiKey>;
    },
    [fetch],
  );
}

function useAddApiKeyToState() {
  const [apiKeys, setApiKeys] = useApiKeysState();

  return useCallback(
    (apiKey: ApiKey) => {
      setApiKeys([apiKey, ...apiKeys]);
    },
    [apiKeys, setApiKeys],
  );
}
