import React from 'react';
import {View, ActivityIndicator} from 'react-native';
import {Text, makeStyles} from '@rneui/themed';

export const useStyles = makeStyles(theme => ({
  container: {
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
}));

export function LoadingIndicator(props: Props) {
  const styles = useStyles();

  return (
    <View style={styles.container}>
      <View style={styles.rowContainer}>
        <Text>{props.message}</Text>
        <ActivityIndicator size="large" style={styles.activityIndicator} />
      </View>
    </View>
  );
}

interface Props {
  message: string;
}
