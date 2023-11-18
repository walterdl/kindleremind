import {makeStyles} from '@rneui/themed';

export const useApiKeyCardStyles = makeStyles(theme => ({
  container: {
    margin: 0,
    marginBottom: theme.spacing.md,
  },
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

export const useCreateApiKeyStyles = makeStyles(theme => ({
  addButtonContainer: {
    position: 'absolute',
    right: 0,
    bottom: theme.spacing.xl + theme.spacing.xl,
    width: 'auto',
    height: 'auto',
    display: 'flex',
  },
  overlayContainer: {
    width: 250,
  },
  title: {
    fontWeight: 'bold',
    fontSize: 18,
    textAlign: 'center',
    marginBottom: theme.spacing.xl,
  },
  error: {
    color: theme.colors.error,
    maxWidth: 200,
    alignSelf: 'center',
    textAlign: 'center',
    marginTop: theme.spacing.md,
  },
}));
