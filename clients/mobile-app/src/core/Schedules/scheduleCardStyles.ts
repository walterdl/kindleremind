import {makeStyles} from '@rneui/themed';

export const useStyles = makeStyles(theme => ({
  container: {
    margin: 0,
    marginBottom: theme.spacing.md,
  },
  content: {
    gap: theme.spacing.md,
  },
  time: {
    fontWeight: 'bold',
  },
  optionsContainer: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginTop: theme.spacing.md,
  },
  deleteButtonStyle: {
    borderColor: theme.colors.error,
  },
  deleteButtonLabelStyle: {
    color: theme.colors.error,
  },
}));
