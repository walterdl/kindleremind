export interface ReminderSchedule {
  id: string;
  /**
   * ISO 8601.
   */
  datetime: string;
  /**
   * 0 - 6, 0 is Sunday, 6 is Saturday
   */
  weekdays: Weekdays;
}

export type Weekday = '0' | '1' | '2' | '3' | '4' | '5' | '6';

export type Weekdays = Weekday[];
