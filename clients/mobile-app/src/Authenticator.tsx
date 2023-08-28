import React from 'react';
import {useState} from 'react';
import {View} from 'react-native';
import {Input} from '@rneui/themed';

// import { makeStyles } from '@rneui/themed';

// makeStyles({

// })

export function Authenticator() {
  const [apiKey, setApiKey] = useState('');

  return (
    <View>
      <Input
        value={apiKey}
        onChangeText={setApiKey}
        placeholder="Enter API Key"
        label="API Key"
      />
    </View>
  );
}
