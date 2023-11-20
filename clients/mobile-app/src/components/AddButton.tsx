import React from 'react';
import {View} from 'react-native';
import {Button, Icon, makeStyles} from '@rneui/themed';

export const useStyles = makeStyles(theme => ({
  container: {
    position: 'absolute',
    right: 0,
    bottom: theme.spacing.xl + theme.spacing.xl,
    width: 'auto',
    height: 'auto',
    display: 'flex',
  },
  button: {
    width: 60,
    height: 60,
    borderRadius: 30,
  },
}));

export function AddButton(props: Props) {
  const styles = useStyles();

  return (
    <View style={styles.container}>
      <Button
        buttonStyle={styles.button}
        containerStyle={styles.button}
        type="solid"
        onPress={props.onPress}>
        <Icon name="add" />
      </Button>
    </View>
  );
}

interface Props {
  onPress: () => void;
}
