import {useCallback, useEffect, useRef, useState} from 'react';

import {useFetch, Fetch} from '../../utils/useFetch';
import type {ApiKey} from './types';
import {useApiKeysState} from './apiKeysState';

export function useGetApiKeys() {
  const fetch = useFetch();
  const [, setApiKeys] = useApiKeysState();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);

  const getApiKeys = useCallback(async () => {
    setLoading(true);
    setError(false);

    try {
      const result = await fetchApiKeys(fetch);
      setApiKeys(result);
    } catch {
      setError(true);
    } finally {
      setLoading(false);
    }
  }, [fetch, setApiKeys]);

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

  const data: ApiKey[] = await response.json();

  return data || [];
}
