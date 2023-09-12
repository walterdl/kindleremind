import type {NativeStackNavigationProp} from '@react-navigation/native-stack';

export enum RootScreenNames {
  CheckLogin = 'CheckLogin',
  Login = 'Login',
  PrivateRoot = 'PrivateRoot',
}

export type RootStackParamList = {
  [RootScreenNames.CheckLogin]: undefined;
  [RootScreenNames.Login]: undefined;
  [RootScreenNames.PrivateRoot]: undefined;
};

export enum PrivateRootScreenNames {
  Clippings = 'Clippings',
}

export type PrivateRootStackParamList = {
  [PrivateRootScreenNames.Clippings]: undefined;
};

export type PrivateRootScreenNavigationProp = NativeStackNavigationProp<
  RootStackParamList,
  RootScreenNames.PrivateRoot
>;
