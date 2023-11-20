import React, {createContext, useContext, useState, ReactElement} from 'react';
import {ReminderSchedule} from './types';

const initialState: ReminderSchedulesState = [
  [],
  () => {
    /* Empty */
  },
];
const SchedulesContext = createContext<ReminderSchedulesState>(initialState);

export function useSchedulesState() {
  const context = useContext(SchedulesContext);

  if (!context) {
    throw new Error('useSchedulesState must be used within a SchedulesContext');
  }

  return context;
}

export function ReminderSchedulesStateProvider(props: {
  children: ReactElement;
}) {
  const [schedules, setSchedules] = useState<ReminderSchedule[]>([]);

  return (
    <SchedulesContext.Provider value={[schedules, setSchedules]}>
      {props.children}
    </SchedulesContext.Provider>
  );
}

type ReminderSchedulesState = [
  ReminderSchedule[],
  (schedules: ReminderSchedule[]) => void,
];
