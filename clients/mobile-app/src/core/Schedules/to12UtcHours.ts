export function to12UtcHours(datetime: string | Date) {
  const date = datetime instanceof Date ? datetime : new Date(datetime);

  const formatter = new Intl.DateTimeFormat('en-US', {
    hour: 'numeric',
    minute: 'numeric',
    hour12: true,
    timeZone: 'UTC',
  });

  return formatter.format(date);
}
