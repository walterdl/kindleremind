import React from 'react';
import {View} from 'react-native';
import {Button} from '@rneui/themed';

import {Weekday, Weekdays} from './types';
import {useStyles} from './daysStyles';

const WEEKDAY_NAMES = {
  '0': 'S',
  '1': 'M',
  '2': 'T',
  '3': 'W',
  '4': 'T',
  '5': 'F',
  '6': 'S',
};

export function Days(props: Props) {
  const styles = useStyles();

  return (
    <View style={styles.container}>
      {Object.keys(WEEKDAY_NAMES).map(day => {
        const selected = (props.value || []).includes(day as Weekday);

        const disabledStyle = selected
          ? styles.selectedDisabled
          : styles.notSelectedDisabled;

        const disabledTitleStyle = selected
          ? styles.selectedDisabledTitle
          : styles.notSelectedDisabledTitle;

        return (
          <Button
            key={day}
            type={selected ? 'solid' : 'outline'}
            containerStyle={styles.button}
            buttonStyle={styles.button}
            disabledStyle={disabledStyle}
            disabledTitleStyle={disabledTitleStyle}
            disabled={props.readonly}
            title={WEEKDAY_NAMES[day as Weekday]}
          />
        );
      })}
    </View>
  );
}

interface Props {
  value?: Weekdays;
  /**
   * @default false
   */
  readonly?: boolean;
  onChange?: (value: Weekdays) => void;
}
