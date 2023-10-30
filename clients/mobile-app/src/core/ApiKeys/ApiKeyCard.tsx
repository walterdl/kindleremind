import React, {useCallback, useState} from 'react';
import {View} from 'react-native';
import {Text, Button, Card, Icon} from '@rneui/themed';
import Clipboard from '@react-native-clipboard/clipboard';

import {apiKeyCardStyles} from './styles';
import {ApiKey} from './types';

export function ApiKeyCard(props: {apiKey: ApiKey}) {
  const {apiKey} = props;
  const styles = apiKeyCardStyles();
  const [revealed, setRevealed] = useState(false);

  // hidePlaceholder var equal to the first 7 chars + 10 asterisks
  const hidePlaceholder = apiKey.value.slice(0, 10) + '**********';
  const keyEllipsisMoe = revealed ? undefined : 'tail';
  const keyNumberOfLines = revealed ? undefined : 1;

  return (
    <Card>
      <Card.Title>{apiKey.name}</Card.Title>
      <Card.Divider />
      <View>
        <View style={styles.valueLabelContainer}>
          <Text
            style={styles.textLine}
            ellipsizeMode={keyEllipsisMoe}
            numberOfLines={keyNumberOfLines}
            selectable>
            <Text style={styles.valueLabel}>Value:</Text>{' '}
            <Text>{revealed ? apiKey.value : hidePlaceholder}</Text>
          </Text>
        </View>
        <Text style={styles.textLine}>
          Crated {new Date(apiKey.createdAt).toString()}
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
          <CopyToClipboardButton apiKeyValue={apiKey.value} />
          <Button
            color="error"
            type="outline"
            containerStyle={styles.optionContainer}
            buttonStyle={styles.deleteButtonStyle}
            titleStyle={styles.deleteButtonLabelStyle}>
            Delete
            <Icon name="delete" color={styles.deleteButtonLabelStyle.color} />
          </Button>
        </View>
      </View>
    </Card>
  );
}

function CopyToClipboardButton(props: {apiKeyValue: string}) {
  const styles = apiKeyCardStyles();

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
