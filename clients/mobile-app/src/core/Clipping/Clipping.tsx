import React from 'react';
import {NativeStackScreenProps} from '@react-navigation/native-stack';
import {Text} from '@rneui/themed';
import dayjs from 'dayjs';

import {useStyles} from './styles';
import {RootStackParamList, RootScreenNames} from '../Navigation';
import {ScreenContainer} from '../../components/ScreenContainer';
import {Clipping} from './types';
import {ScrollView} from 'react-native';

export function ClippingView(props: Props) {
  const styles = useStyles();
  const clipping = props.route.params.clipping;
  const position = formatPosition(clipping);

  return (
    <ScreenContainer>
      <ScrollView>
        <Text style={styles.title} selectable>
          {clipping.title}
        </Text>
        <Text style={styles.author} selectable>
          <Text>by</Text>{' '}
          <Text style={styles.authorText}>{clipping.author}</Text>
        </Text>
        <Text style={styles.content} selectable>
          <Text style={styles.quotationMark}>“</Text>
          <Text style={styles.contentText}>{clipping.content}</Text>
          <Text style={styles.quotationMark}>”</Text>
        </Text>
        {!!position && (
          <Text style={styles.position} selectable>
            {position}
          </Text>
        )}
        <Text style={styles.date} selectable>
          Highlight taken on {formatClippingDate(clipping.timestamp)}
        </Text>
      </ScrollView>
    </ScreenContainer>
  );
}

function formatClippingDate(timestamp: string): string {
  return dayjs(new Date(timestamp)).locale('en').format('MMM D, YYYY, h:mm A');
}

function formatPosition(clipping: Clipping) {
  const elements = [];

  if (clipping.position.page) {
    elements.push(`page ${clipping.position.page}`);
  }

  if (clipping.position.location) {
    elements.push(`location ${clipping.position.location}`);
  }

  const result = elements.join(', ');
  return result.charAt(0).toUpperCase() + result.slice(1);
}

type Props = NativeStackScreenProps<
  RootStackParamList,
  RootScreenNames.ClippingView
>;
