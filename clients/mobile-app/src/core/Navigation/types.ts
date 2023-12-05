import {Clipping} from '../Clipping';

export enum RootScreenNames {
  Home = 'Home',
  ApiKeys = 'ApiKeys',
  Schedules = 'Schedules',
  ClippingView = 'Clipping',
}

export type RootStackParamList = {
  [RootScreenNames.Home]: undefined;
  [RootScreenNames.ApiKeys]: undefined;
  [RootScreenNames.Schedules]: undefined;
  [RootScreenNames.ClippingView]: {
    clipping: Clipping;
  };
};
