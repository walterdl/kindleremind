import {useCallback, useEffect, useRef, useState} from 'react';

import {Fetch, useFetch} from '../../utils/useFetch';
import {ReminderSchedule} from './types';

export function useGetSchedules() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const [schedules, setSchedules] = useState<ReminderSchedule[]>([]);
  const fetch = useFetch();

  const refetch = useCallback(async () => {
    setLoading(true);
    setError(false);

    try {
      setSchedules(await fetchSchedules(fetch));
    } catch {
      setError(true);
    } finally {
      setLoading(false);
    }
  }, [fetch]);

  useInitialFetch(refetch);

  return {refetch, loading, error, schedules};
}

function useInitialFetch(refetch: () => void) {
  const executed = useRef(false);
  useEffect(() => {
    if (executed.current) {
      return;
    }

    refetch();
    executed.current = true;
  }, [refetch]);
}

async function fetchSchedules(fetch: Fetch) {
  const response = await fetch('/schedules');

  if (!response.ok) {
    throw new Error('Invalid schedules response');
  }

  const data: ReminderSchedule[] = await response.json();

  return data || [];
}
