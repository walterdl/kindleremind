import React, {createContext, useContext, useState, ReactElement} from 'react';
import {ApiKey} from './types';

const initialState: ApiKeysState = [
  [],
  () => {
    /* Empty */
  },
];
const ApiKeysContext = createContext<ApiKeysState>(initialState);

export function useApiKeysState() {
  const context = useContext(ApiKeysContext);

  if (!context) {
    throw new Error('useApiKeysContext must be used within a ApiKeysContext');
  }

  return context;
}

export function ApiKeysStateProvider(props: {children: ReactElement}) {
  const [apiKeys, setApiKeys] = useState<ApiKey[]>([]);

  return (
    <ApiKeysContext.Provider value={[apiKeys, setApiKeys]}>
      {props.children}
    </ApiKeysContext.Provider>
  );
}

export type ApiKeysState = [ApiKey[], (apiKeys: ApiKey[]) => void];
