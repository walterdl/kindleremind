import React, {useEffect} from 'react';
import {ActivityIndicator, View} from 'react-native';
import {Text, Button, Card, Icon} from '@rneui/themed';
import {ALERT_TYPE, Toast} from 'react-native-alert-notification';

import {useStyles} from './scheduleCardStyles';
import {ReminderSchedule} from './types';
import {to12Hours} from './to12Hours';
import {Days} from './Days';
import {useDeleteSchedule} from './useDeleteSchedule';

export function ScheduleCard(props: Props) {
  const styles = useStyles();
  const {deleteSchedule, error, loading} = useDeleteSchedule();

  useEffect(() => {
    if (error) {
      Toast.show({
        type: ALERT_TYPE.DANGER,
        title: 'Error',
        textBody: "Couldn't delete schedule. Please, try again.",
        autoClose: true,
        onPress: () => {
          Toast.hide();
        },
      });
    }
  }, [error]);

  return (
    <Card containerStyle={styles.container}>
      <View style={styles.content}>
        <Text>
          Repeats at{' '}
          <Text style={styles.time}>{to12Hours(props.schedule.datetime)}</Text>{' '}
          on:
        </Text>
        <Days value={props.schedule.weekdays} readonly />
        <View style={styles.optionsContainer}>
          <Button
            buttonStyle={styles.deleteButtonStyle}
            titleStyle={styles.deleteButtonLabelStyle}
            color="error"
            type="outline"
            disabled={loading}
            onPress={() => deleteSchedule(props.schedule)}>
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

interface Props {
  schedule: ReminderSchedule;
}
