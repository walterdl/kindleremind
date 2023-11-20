import React, {useCallback, useEffect, useState} from 'react';
import {View} from 'react-native';
import {Overlay, Button, Text} from '@rneui/themed';
import {DateTimePickerAndroid} from '@react-native-community/datetimepicker';

import {AddButton} from '../../components/AddButton';
import {Days} from './Days';
import {useStyles} from './createScheduleStyles';
import {to12UtcHours} from './to12UtcHours';
import {Weekday} from './types';
import {useCreateSchedule} from './useCreateSchedule';

export function CreateSchedule() {
  const styles = useStyles();
  const [visible, setVisible] = useState(false);
  const [time, setTime] = useState(new Date());
  const [weekdays, setWeekdays] = useState<Weekday[]>([]);
  const {createSchedule, loading, error, cleanError} = useCreateSchedule({
    onSuccess: () => setVisible(false),
  });
  const triggerCreation = useCallback(() => {
    createSchedule({
      id: '',
      datetime: time.toISOString(),
      weekdays,
    });
  }, [createSchedule, time, weekdays]);

  const showTimePicker = useCallback(() => {
    DateTimePickerAndroid.open({
      value: time,
      onChange: event => {
        setTime(new Date(event.nativeEvent.timestamp));
      },
      mode: 'time',
      is24Hour: false,
      timeZoneName: 'UTC',
    });
  }, [time]);

  useResetWhenClosed({
    visible,
    cleanError,
    setTime,
    setWeekdays,
  });

  return (
    <>
      <AddButton onPress={() => setVisible(true)} />
      <Overlay
        isVisible={visible}
        onBackdropPress={() => {
          if (loading) {
            return;
          }

          setVisible(false);
        }}>
        <Text style={styles.description}>
          Set your reminders by selecting a time and the weekdays when you want
          to receive notifications.
        </Text>
        <View style={styles.inputGroup}>
          <Text style={styles.label}>UTC Time: </Text>
          <View style={styles.timeButtonContainer}>
            <Button
              title={to12UtcHours(time)}
              type="outline"
              onPress={showTimePicker}
            />
          </View>
        </View>
        <View style={styles.inputGroup}>
          <Text style={styles.label}>Days: </Text>
          <Days value={weekdays} onChange={setWeekdays} />
        </View>
        <Button
          containerStyle={styles.createButton}
          title="Create"
          loading={loading}
          disabled={weekdays.length === 0}
          onPress={triggerCreation}
        />
        {error && (
          <Text style={styles.error}>
            There was an error creating the reminder time.{'\n'}Please, try
            again
          </Text>
        )}
      </Overlay>
    </>
  );
}

function useResetWhenClosed({
  cleanError,
  setTime,
  setWeekdays,
  visible,
}: UseResetViewInput) {
  useEffect(() => {
    if (visible) {
      return;
    }

    setWeekdays([]);
    setTime(new Date());
    cleanError();
  }, [cleanError, setTime, setWeekdays, visible]);
}

interface UseResetViewInput {
  visible: boolean;
  setWeekdays: (weekdays: Weekday[]) => void;
  setTime: (time: Date) => void;
  cleanError: () => void;
}
