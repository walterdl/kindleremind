import {makeStyles} from '@rneui/themed';

export const useStyles = makeStyles(theme => ({
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: theme.spacing.md,
    color: theme.colors.primary,
  },
  author: {
    fontSize: 17,
    marginBottom: theme.spacing.xl,
  },
  authorText: {
    fontWeight: '700',
  },
  content: {
    borderLeftWidth: 4,
    borderLeftColor: theme.colors.primary,
    paddingLeft: theme.spacing.lg,
    fontSize: 17,
    marginBottom: theme.spacing.xl,
  },
  contentText: {
    fontStyle: 'italic',
  },
  quotationMark: {
    fontWeight: 'bold',
    fontSize: 24,
  },
  position: {
    marginBottom: theme.spacing.sm,
  },
  date: {
    marginBottom: theme.spacing.xl,
  },
}));
