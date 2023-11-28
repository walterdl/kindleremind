import {useCallback, useState} from 'react';

import {useFetch} from '../../utils/useFetch';
import {useSchedulesState} from './schedulesState';
import {ReminderSchedule} from './types';

export function useDeleteSchedule() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);
  const [schedules, setSchedules] = useSchedulesState();
  const sendDeletion = useDelete();

  const deleteSchedule = useCallback(
    async (schedule: ReminderSchedule) => {
      setLoading(true);
      setError(false);

      try {
        await sendDeletion(schedule);
        setSchedules(schedules.filter(k => k.id !== schedule.id));
      } catch {
        setError(true);
      } finally {
        setLoading(false);
      }
    },
    [schedules, sendDeletion, setSchedules],
  );

  return {loading, error, deleteSchedule};
}

function useDelete() {
  const fetch = useFetch();

  return useCallback(
    async (schedule: ReminderSchedule) => {
      const response = await fetch('/schedules', {
        method: 'delete',
        queryParams: {id: schedule.id},
      });

      if (!response.ok) {
        throw new Error('Could not delete schedule');
      }
    },
    [fetch],
  );
}
