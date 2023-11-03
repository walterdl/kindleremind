import React, {useCallback, useEffect, useState} from 'react';
import {View, ActivityIndicator} from 'react-native';
import {Text, Button, Card, Icon} from '@rneui/themed';
import Clipboard from '@react-native-clipboard/clipboard';
import {ALERT_TYPE, Toast} from 'react-native-alert-notification';

import {useApiKeyCardStyles} from './styles';
import {ApiKey} from './types';
import {useDeleteApiKey} from './useDeleteApiKey';

export function ApiKeyCard(props: Props) {
  const styles = useApiKeyCardStyles();
  const [revealed, setRevealed] = useState(false);
  const {deleteApiKey, loading, error} = useDeleteApiKey();

  // hidePlaceholder var equal to the first 7 chars + 10 asterisks
  const hidePlaceholder = props.apiKey.value.slice(0, 10) + '**********';
  const keyEllipsisMoe = revealed ? undefined : 'tail';
  const keyNumberOfLines = revealed ? undefined : 1;

  useEffect(() => {
    if (error) {
      Toast.show({
        type: ALERT_TYPE.DANGER,
        title: 'Error',
        textBody: "Couldn't delete API Key. Please, try again.",
        autoClose: true,
        onPress: () => {
          Toast.hide();
        },
      });
    }
  }, [error]);

  return (
    <Card>
      <Card.Title>{props.apiKey.name}</Card.Title>
      <Card.Divider />
      <View>
        <View style={styles.valueLabelContainer}>
          <Text
            style={styles.textLine}
            ellipsizeMode={keyEllipsisMoe}
            numberOfLines={keyNumberOfLines}
            selectable>
            <Text style={styles.valueLabel}>Value:</Text>{' '}
            <Text>{revealed ? props.apiKey.value : hidePlaceholder}</Text>
          </Text>
        </View>
        <Text style={styles.textLine}>
          Crated {new Date(props.apiKey.createdAt).toString()}
        </Text>
        <View style={styles.optionsContainer}>
          <Button
            type="outline"
            containerStyle={styles.optionContainer}
            onPress={() => setRevealed(!revealed)}>
            {revealed ? 'Hide' : 'Reveal'}{' '}
            <Icon
              name={revealed ? 'visibility-off' : 'visibility'}
              color={styles.normalIcon.color}
            />
          </Button>
          <CopyToClipboardButton apiKeyValue={props.apiKey.value} />
          <Button
            color="error"
            type="outline"
            containerStyle={styles.optionContainer}
            buttonStyle={styles.deleteButtonStyle}
            titleStyle={styles.deleteButtonLabelStyle}
            disabled={loading}
            onPress={() => deleteApiKey(props.apiKey)}>
            Delete{' '}
            {loading ? (
              <ActivityIndicator />
            ) : (
              <Icon name="delete" color={styles.deleteButtonLabelStyle.color} />
            )}
          </Button>
        </View>
      </View>
    </Card>
  );
}

function CopyToClipboardButton(props: {apiKeyValue: string}) {
  const styles = useApiKeyCardStyles();

  const [copied, setCopied] = useState(false);

  const copy = useCallback(() => {
    Clipboard.setString(props.apiKeyValue);
    setCopied(true);
    const timeoutId = setTimeout(() => setCopied(false), 2000);

    return () => {
      clearTimeout(timeoutId);
    };
  }, [props.apiKeyValue]);

  return (
    <Button
      type="outline"
      containerStyle={styles.optionContainer}
      onPress={copy}>
      Copy{' '}
      {copied ? (
        <Icon name="done" color={styles.normalIcon.color} />
      ) : (
        <Icon name="content-copy" color={styles.normalIcon.color} />
      )}
    </Button>
  );
}

interface Props {
  apiKey: ApiKey;
}
