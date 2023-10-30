import {useCallback, useEffect, useRef, useState} from 'react';
import {useFetch, Fetch} from '../../utils/useFetch';
import {ApiKey, ApiKeysResponse} from './types';

export function useGetApiKeys(receiveApiKeys: (apiKeys: ApiKey[]) => void) {
  const fetch = useFetch();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);

  const getApiKeys = useCallback(async () => {
    setLoading(true);
    setError(false);

    try {
      const result = await fetchApiKeys(fetch);
      receiveApiKeys(result);
    } catch {
      setError(true);
    } finally {
      setLoading(false);
    }
  }, [fetch, receiveApiKeys]);

  const executed = useRef(false);
  useEffect(() => {
    if (executed.current) {
      return;
    }

    getApiKeys();
    executed.current = true;
  }, [getApiKeys]);

  return {loading, error, getApiKeys};
}

async function fetchApiKeys(fetch: Fetch) {
  const response = await fetch('/api-keys');

  if (!response.ok) {
    throw new Error();
  }

  const data: ApiKeysResponse = await response.json();

  return data.apiKeys || [];
}
