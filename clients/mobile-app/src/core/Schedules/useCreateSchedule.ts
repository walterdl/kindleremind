import {useCallback, useState} from 'react';

import {useFetch} from '../../utils/useFetch';
import {ReminderSchedule} from './types';
import {useSchedulesState} from './schedulesState';

export function useCreateSchedule(options: UseCreateScheduleOptions) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);
  const post = usePost();
  const addScheduleToState = useAddScheduleToState();
  const {onSuccess} = options;

  const createSchedule = useCallback(
    async (schedule: ReminderSchedule) => {
      try {
        setLoading(true);
        setError(false);
        addScheduleToState(await post(schedule));
        onSuccess?.();
      } catch {
        setError(true);
      } finally {
        setLoading(false);
      }
    },
    [addScheduleToState, onSuccess, post],
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

function useAddScheduleToState() {
  const [schedules, setSchedules] = useSchedulesState();

  return useCallback(
    (apiKey: ReminderSchedule) => {
      setSchedules([apiKey, ...schedules]);
    },
    [schedules, setSchedules],
  );
}

export interface UseCreateScheduleOptions {
  onSuccess?: () => void;
}
