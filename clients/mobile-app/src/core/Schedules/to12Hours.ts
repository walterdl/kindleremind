export function to12Hours(time: string) {
  const [hours, minutes, seconds] = time.split(':');
  const date = new Date();
  date.setHours(Number(hours), Number(minutes), Number(seconds));

  const formatter = new Intl.DateTimeFormat('en-US', {
    hour: 'numeric',
    minute: 'numeric',
    hour12: true,
  });

  return formatter.format(date);
}
