import React, {useMemo} from 'react';
import {StyleProp, View, ViewStyle} from 'react-native';
import {Button, Text, Icon, makeStyles} from '@rneui/themed';

const useStyles = makeStyles(theme => ({
  root: {
    backgroundColor: '#3b171a',
    borderWidth: 1.5,
    borderColor: '#842029',
    color: '#ea868f',
    position: 'relative',
    padding: theme.spacing.md,
    minHeight: 60,
    borderRadius: theme.spacing.sm,
  },
  text: {
    color: '#ea868f',
  },
  iconContainer: {
    position: 'absolute',
    top: 0,
    right: 0,
  },
  button: {
    backgroundColor: '#653431',
  },
}));

export function ErrorMessage(props: ErrorMessageProps) {
  const styles = useStyles();

  const rootStyles = useMemo(() => {
    const result: StyleProp<ViewStyle>[] = [styles.root];

    if (props.style) {
      result.push(props.style);
    }

    return result;
  }, [props.style, styles.root]);

  if (props.message) {
    return (
      <View style={rootStyles}>
        <Text style={styles.text}>{props.message}</Text>
        <View style={styles.iconContainer}>
          <Button type="solid" size="md" buttonStyle={styles.button}>
            <Icon name="close" type="material" onPress={props.onClose} />
          </Button>
        </View>
      </View>
    );
  }

  return null;
}

interface ErrorMessageProps {
  message: string;
  /**
   * Styles applied to the root element.
   */
  style?: StyleProp<ViewStyle>;
  onClose: () => void;
}
