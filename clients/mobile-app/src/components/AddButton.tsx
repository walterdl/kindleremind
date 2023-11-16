import React from 'react';
import {Button, Icon, makeStyles} from '@rneui/themed';

export const useStyles = makeStyles(() => ({
  button: {
    width: 60,
    height: 60,
    borderRadius: 30,
  },
}));

export function AddButton(props: Props) {
  const styles = useStyles();

  return (
    <Button
      buttonStyle={styles.button}
      containerStyle={styles.button}
      type="solid"
      onPress={props.onPress}>
      <Icon name="add" />
    </Button>
  );
}

interface Props {
  onPress: () => void;
}
