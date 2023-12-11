export function to12Hours(datetime: string | Date) {
  const date = datetime instanceof Date ? datetime : new Date(datetime);

  const formatter = new Intl.DateTimeFormat('en-US', {
    hour: 'numeric',
    minute: 'numeric',
    hour12: true,
  });

  return formatter.format(date);
}
