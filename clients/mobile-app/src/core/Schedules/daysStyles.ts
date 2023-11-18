import {makeStyles} from '@rneui/themed';

export const useStyles = makeStyles(theme => ({
  container: {
    flexDirection: 'row',
    gap: theme.spacing.sm,
  },
  button: {
    width: 45,
    height: 45,
    borderRadius: 45 / 2,
  },
  selectedDisabled: {
    backgroundColor: theme.colors.primary,
  },
  selectedDisabledTitle: {
    color: theme.colors.black,
  },
  notSelectedDisabled: {
    backgroundColor: 'transparent',
    borderColor: theme.colors.primary,
  },
  notSelectedDisabledTitle: {
    color: theme.colors.primary,
  },
}));
