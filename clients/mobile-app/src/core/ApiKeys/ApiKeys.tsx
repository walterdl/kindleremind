import React from 'react';
import {View, ScrollView} from 'react-native';

import {useGetApiKeys} from './useGetApiKeys';
import {ApiKeyCard} from './ApiKeyCard';
import {ApiKeysStateProvider, useApiKeysState} from './apiKeysState';
import {CreateApiKey} from './CreateApiKey';
import {ScreenContainer} from '../../components/ScreenContainer';
import {LoadingIndicator} from '../../components/LoadingIndicator';
import {EmptyIndicator} from '../../components/EmptyIndicator';
import {ErrorIndicator} from '../../components/ErrorIndicator';

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
      {loading && <LoadingIndicator message="Loading keys ..." />}
      {error && <ErrorIndicator onReload={getApiKeys} />}
      {showEmptyIndicator && (
        <EmptyIndicator message={'You have no API Keys'} />
      )}
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
