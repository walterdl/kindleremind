import {useApiKeysState} from './apiKeysState';
import {ApiKey} from './types';
import {useFetch} from '../../utils/useFetch';
import {useCallback, useState} from 'react';

export function useDeleteApiKey() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);
  const [apiKeys, setApiKeys] = useApiKeysState();
  const fetch = useFetch();

  const deleteApiKey = useCallback(
    async (apiKey: ApiKey) => {
      setLoading(true);
      setError(false);

      try {
        const response = await fetch('/api-keys', {
          method: 'delete',
          queryParams: {id: apiKey.id},
        });

        if (!response.ok) {
          throw new Error();
        }

        setApiKeys(apiKeys.filter(k => k.value !== apiKey.value));
      } catch {
        setError(true);
      } finally {
        setLoading(false);
      }
    },
    [apiKeys, fetch, setApiKeys],
  );

  return {loading, error, deleteApiKey};
}
