import React, {useCallback} from 'react';
import {View} from 'react-native';
import {Text, Button, makeStyles} from '@rneui/themed';
import {useNavigation, RootScreenNames} from './Navigation';

const useStyles = makeStyles(theme => ({
  title: {
    fontSize: 18,
    marginBottom: theme.spacing.md,
  },
  space: {
    marginBottom: theme.spacing.xl,
  },
}));

export function Home() {
  const styles = useStyles();
  const navigation = useNavigation();
  const goToApiKeys = useCallback(() => {
    navigation.navigate(RootScreenNames.ApiKeys);
  }, [navigation]);

  return (
    <View>
      <Text style={styles.title}>Setup complete!</Text>
      <Text>
        You'll receive push notifications for your Kindle clippings reminders
      </Text>
      <View style={styles.space} />
      <Button title="API Keys" onPress={goToApiKeys} />
    </View>
  );
}
