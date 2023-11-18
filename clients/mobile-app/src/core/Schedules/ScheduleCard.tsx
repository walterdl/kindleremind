import React from 'react';
import {View} from 'react-native';
import {Text, Button, Card, Icon} from '@rneui/themed';

import {useStyles} from './scheduleCardStyles';
import {ReminderSchedule} from './types';
import {to12Hours} from './to12Hours';
import {Days} from './Days';

export function ScheduleCard(props: Props) {
  const styles = useStyles();

  return (
    <Card containerStyle={styles.container}>
      <View style={styles.content}>
        <Text>
          Repeats at{' '}
          <Text style={styles.time}>{to12Hours(props.schedule.time)}</Text>{' '}
          <Text>({props.schedule.timezone})</Text> on:
        </Text>
        <Days value={props.schedule.weekdays} readonly />
        <View style={styles.optionsContainer}>
          <Button
            buttonStyle={styles.deleteButtonStyle}
            titleStyle={styles.deleteButtonLabelStyle}
            color="error"
            type="outline">
            Delete{' '}
            <Icon name="delete" color={styles.deleteButtonLabelStyle.color} />
          </Button>
        </View>
      </View>
    </Card>
  );
}

interface Props {
  schedule: ReminderSchedule;
}
