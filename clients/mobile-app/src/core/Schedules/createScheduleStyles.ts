import {makeStyles} from '@rneui/themed';

export const useStyles = makeStyles(theme => ({
  timeContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: theme.spacing.md,
  },
  description: {
    marginBottom: theme.spacing.md,
  },
  label: {
    fontWeight: '700',
    marginBottom: theme.spacing.sm,
  },
  inputGroup: {
    marginBottom: theme.spacing.md,
  },
  timeButtonContainer: {
    flexDirection: 'row',
  },
  createButton: {
    marginTop: theme.spacing.md,
  },
  error: {
    color: theme.colors.error,
    alignSelf: 'center',
    textAlign: 'center',
    marginTop: theme.spacing.md,
  },
}));
