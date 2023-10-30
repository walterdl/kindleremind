import React from 'react';
import {View, ActivityIndicator, ScrollView} from 'react-native';
import {Text, Button} from '@rneui/themed';

import {useStyles} from './styles';
import {useGetApiKeys} from './useGetApiKeys';
import {ApiKeyCard} from './ApiKeyCard';
import {ApiKeysStateProvider, useApiKeysState} from './apiKeysState';

export function ApiKeysView() {
  return (
    <ApiKeysStateProvider>
      <ApiKeysContent />
    </ApiKeysStateProvider>
  );
}

function ApiKeysContent() {
  const styles = useStyles();
  const [apiKeys] = useApiKeysState();
  let {loading, error, getApiKeys} = useGetApiKeys();

  return (
    <View>
      <LoadingIndicator loading={loading} />
      <ErrorIndicator error={error} getApiKeys={getApiKeys} />
      <ScrollView>
        <View style={styles.cardsContainer}>
          {!!apiKeys.length &&
            apiKeys.map((apiKey, i) => <ApiKeyCard key={i} apiKey={apiKey} />)}
        </View>
      </ScrollView>
    </View>
  );
}

function LoadingIndicator(props: {loading: boolean}) {
  const styles = useStyles();

  if (props.loading) {
    return (
      <View style={styles.loadingIndicator}>
        <View style={styles.rowContainer}>
          <Text>Loading keys ...</Text>
          <ActivityIndicator size="large" style={styles.activityIndicator} />
        </View>
      </View>
    );
  }

  return null;
}

function ErrorIndicator(props: {error: boolean; getApiKeys: () => void}) {
  const styles = useStyles();

  if (props.error) {
    return (
      <View style={styles.errorContainer}>
        <View style={styles.errorTextContainer}>
          <Text>Something went wrong. Please, try again.</Text>
        </View>
        <View style={styles.reloadContainer}>
          <Button title="Reload" onPress={props.getApiKeys} />
        </View>
      </View>
    );
  }

  return null;
}
