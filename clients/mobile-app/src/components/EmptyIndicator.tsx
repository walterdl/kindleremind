import React from 'react';
import {View, Image} from 'react-native';
import {Text, makeStyles} from '@rneui/themed';

export const useStyles = makeStyles(() => ({
  container: {
    justifyContent: 'center',
    alignItems: 'center',
    flex: 1,
    marginTop: -60,
  },
  imageContainer: {
    width: 200,
    alignItems: 'center',
  },
  image: {
    width: '100%',
    height: undefined,
    aspectRatio: 1,
  },
  text: {
    textAlign: 'center',
  },
}));

export function EmptyIndicator(props: Props) {
  const styles = useStyles();

  return (
    <View style={styles.container}>
      <View style={styles.imageContainer}>
        <Image
          style={styles.image}
          source={require('./empty.png')}
          resizeMode="contain"
        />
      </View>
      <Text style={styles.text}>{props.message}</Text>
    </View>
  );
}

interface Props {
  message: string;
}
