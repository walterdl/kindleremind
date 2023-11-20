import React from 'react';
import {ScrollView, View} from 'react-native';

import {useGetSchedules} from './useGetSchedules';
import {ScreenContainer} from '../../components/ScreenContainer';
import {LoadingIndicator} from '../../components/LoadingIndicator';
import {EmptyIndicator} from '../../components/EmptyIndicator';
import {ErrorIndicator} from '../../components/ErrorIndicator';
import {ScheduleCard} from './ScheduleCard';
import {CreateSchedule} from './CreateSchedule';

export function Schedules() {
  const {schedules, loading, error, refetch} = useGetSchedules();

  const isEmpty = !loading && !error && schedules.length === 0;
  const showContent = !loading && !error && schedules.length > 0;

  return (
    <ScreenContainer>
      {loading && <LoadingIndicator message="Loading reminder schedules ..." />}
      {isEmpty && (
        <EmptyIndicator
          message={
            "You don't have any reminder schedule. Start creating one to receive your reminders."
          }
        />
      )}
      {error && <ErrorIndicator onReload={refetch} />}
      {showContent && (
        <ScrollView>
          <View>
            {schedules.map((schedule, i) => (
              <ScheduleCard key={i} schedule={schedule} />
            ))}
          </View>
        </ScrollView>
      )}
      {(isEmpty || showContent) && <CreateSchedule />}
    </ScreenContainer>
  );
}
