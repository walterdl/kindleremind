import React from 'react';
import {View, ActivityIndicator, ScrollView, Image} from 'react-native';
import {Text, Button} from '@rneui/themed';

import {
  useEmptyIndicatorStyles,
  useLoadingStyles,
  useErrorIndicatorStyles,
} from './styles';
import {useGetApiKeys} from './useGetApiKeys';
import {ApiKeyCard} from './ApiKeyCard';
import {ApiKeysStateProvider, useApiKeysState} from './apiKeysState';
import {CreateApiKey} from './CreateApiKey';
import {ScreenContainer} from '../../components/ScreenContainer';

export function ApiKeysView() {
  return (
    <ApiKeysStateProvider>
      <ApiKeysContent />
    </ApiKeysStateProvider>
  );
}

function ApiKeysContent() {
  const [apiKeys] = useApiKeysState();
  let {loading, error, getApiKeys} = useGetApiKeys();
  const showApiKeyCreator = !loading && !error;
  const showEmptyIndicator = apiKeys.length === 0 && showApiKeyCreator;

  return (
    <ScreenContainer>
      {loading && <LoadingIndicator />}
      {error && <ErrorIndicator getApiKeys={getApiKeys} />}
      {showEmptyIndicator && <EmptyIndicator />}
      {apiKeys.length > 0 && (
        <ScrollView>
          <View>
            {apiKeys.map((apiKey, i) => (
              <ApiKeyCard key={i} apiKey={apiKey} />
            ))}
          </View>
        </ScrollView>
      )}
      {showApiKeyCreator && <CreateApiKey />}
    </ScreenContainer>
  );
}

function EmptyIndicator() {
  const styles = useEmptyIndicatorStyles();

  return (
    <View style={styles.container}>
      <View style={styles.imageContainer}>
        <Image
          style={styles.image}
          source={require('./empty.png')}
          resizeMode="contain"
        />
      </View>
      <Text style={styles.text}>You have no API Keys</Text>
    </View>
  );
}

function LoadingIndicator() {
  const styles = useLoadingStyles();

  return (
    <View style={styles.container}>
      <View style={styles.rowContainer}>
        <Text>Loading keys ...</Text>
        <ActivityIndicator size="large" style={styles.activityIndicator} />
      </View>
    </View>
  );
}

function ErrorIndicator(props: {getApiKeys: () => void}) {
  const styles = useErrorIndicatorStyles();

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
