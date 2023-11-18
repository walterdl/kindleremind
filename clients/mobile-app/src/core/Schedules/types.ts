export interface ReminderSchedule {
  id: string;
  /**
   * ISO 8601 time part. E.g. 10:00:00
   */
  time: string;
  /**
   * 0 - 6, 0 is Sunday, 6 is Saturday
   */
  weekdays: Weekdays;
  timezone: string;
}

export type Weekday = '0' | '1' | '2' | '3' | '4' | '5' | '6';

export type Weekdays = Weekday[];
