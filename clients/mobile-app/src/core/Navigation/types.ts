export enum RootScreenNames {
  Clippings = 'Clippings',
  ApiKeys = 'ApiKeys',
  Schedules = 'Schedules',
}

export type RootStackParamList = {
  [RootScreenNames.Clippings]: undefined;
  [RootScreenNames.ApiKeys]: undefined;
  [RootScreenNames.Schedules]: undefined;
};
