import React from 'react';
import {View} from 'react-native';
import {Text, Button, makeStyles} from '@rneui/themed';

export const useErrorIndicatorStyles = makeStyles(theme => ({
  errorTextContainer: {
    marginBottom: theme.spacing.md,
  },
  errorContainer: {
    justifyContent: 'center',
    alignItems: 'center',
    height: '100%',
  },
  reloadContainer: {flexDirection: 'row'},
}));

export function ErrorIndicator(props: Props) {
  const styles = useErrorIndicatorStyles();

  return (
    <View style={styles.errorContainer}>
      <View style={styles.errorTextContainer}>
        <Text>Something went wrong. Please, try again.</Text>
      </View>
      <View style={styles.reloadContainer}>
        <Button title="Reload" onPress={props.onReload} />
      </View>
    </View>
  );
}

interface Props {
  onReload: () => void;
}
