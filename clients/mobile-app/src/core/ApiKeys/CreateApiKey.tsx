import React, {useEffect, useState} from 'react';
import {View} from 'react-native';
import {Overlay, Button, Icon, Text, Input} from '@rneui/themed';

import {useCreateApiKeyStyles} from './styles';
import {useCreateApiKey} from './useCreateApiKey';

export function CreateApiKey() {
  const styles = useCreateApiKeyStyles();
  const [visible, setVisible] = useState(false);
  const [name, setName] = useState('');
  const {createApiKey, loading, error, cleanError} = useCreateApiKey();
  const isValid = name.trim().length > 0;
  const disabled = loading || !isValid;

  useEffect(() => {
    if (visible) {
      return;
    }

    setName('');
    cleanError();
  }, [cleanError, visible]);

  return (
    <>
      <View style={styles.addButtonContainer}>
        <Button
          buttonStyle={styles.addButton}
          containerStyle={styles.addButton}
          type="solid"
          onPress={() => setVisible(true)}>
          <Icon name="add" />
        </Button>
      </View>
      <Overlay
        isVisible={visible}
        onBackdropPress={() => {
          if (loading) {
            return;
          }

          setVisible(false);
        }}>
        <View style={styles.overlayContainer}>
          <Text style={styles.title}>Create API Key</Text>
          <Input
            placeholder="Enter API Key Name"
            value={name}
            disabled={loading}
            onChangeText={setName}
          />
        </View>
        <Button
          type="solid"
          title="Create"
          disabled={disabled}
          loading={loading}
          onPress={() => createApiKey(name)}
        />
        {error && (
          <Text style={styles.error}>
            There was an error creating the API Key. Please, try again
          </Text>
        )}
      </Overlay>
    </>
  );
}
