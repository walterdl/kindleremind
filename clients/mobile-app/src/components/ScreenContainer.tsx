import React from 'react';
import {View} from 'react-native';
import {makeStyles} from '@rneui/themed';

const useStyles = makeStyles(theme => ({
  container: {
    marginTop: theme.spacing.md,
    flex: 1,
  },
}));

export function ScreenContainer(props: {children: React.ReactNode}) {
  const styles = useStyles();

  return <View style={styles.container}>{props.children}</View>;
}
