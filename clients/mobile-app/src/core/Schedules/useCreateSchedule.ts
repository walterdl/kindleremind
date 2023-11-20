import {useCallback, useState} from 'react';

import {useFetch} from '../../utils/useFetch';
import {ReminderSchedule} from './types';

export function useCreateSchedule(options: UseCreateScheduleOptions) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);
  const post = usePost();
  const {onSuccess} = options;

  const createSchedule = useCallback(
    async (schedule: ReminderSchedule) => {
      try {
        setLoading(true);
        setError(false);
        await post(schedule);
        onSuccess?.();
      } catch {
        setError(true);
      } finally {
        setLoading(false);
      }
    },
    [onSuccess, post],
  );

  const cleanError = useCallback(() => {
    setError(false);
  }, []);

  return {createSchedule, loading, error, cleanError};
}

function usePost() {
  const fetch = useFetch();

  return useCallback(
    async (schedule: ReminderSchedule) => {
      const response = await fetch('/schedules', {
        body: JSON.stringify(schedule),
        method: 'POST',
      });

      if (!response.ok) {
        throw new Error();
      }

      return response.json() as Promise<ReminderSchedule>;
    },
    [fetch],
  );
}

export interface UseCreateScheduleOptions {
  onSuccess?: () => void;
}
