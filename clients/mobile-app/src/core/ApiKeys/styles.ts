import {makeStyles} from '@rneui/themed';

export const useStyles = makeStyles(theme => ({
  loadingIndicator: {
    height: '100%',
    justifyContent: 'center',
  },
  rowContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
  },
  activityIndicator: {
    marginLeft: theme.spacing.sm,
  },
  errorTextContainer: {
    marginBottom: theme.spacing.md,
  },
  errorContainer: {
    justifyContent: 'center',
    alignItems: 'center',
    height: '100%',
  },
  reloadContainer: {flexDirection: 'row'},
  cardsContainer: {
    flex: 1,
  },
}));

export const apiKeyCardStyles = makeStyles(theme => ({
  valueLabelContainer: {
    flexDirection: 'row',
    position: 'relative',
  },
  valueLabel: {
    fontWeight: 'bold',
  },
  optionsContainer: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginTop: theme.spacing.md,
  },
  optionContainer: {
    marginRight: theme.spacing.md,
  },
  deleteButtonStyle: {
    borderColor: theme.colors.error,
  },
  deleteButtonLabelStyle: {
    color: theme.colors.error,
  },
  normalIcon: {
    color: theme.colors.primary,
  },
  textLine: {
    marginBottom: theme.spacing.sm,
  },
}));
