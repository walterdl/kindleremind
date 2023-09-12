import {NavigatorScreenParams} from '@react-navigation/native';
import type {NativeStackNavigationProp} from '@react-navigation/native-stack';

export enum RootScreenNames {
  Login = 'Login',
  PrivateRoot = 'PrivateRoot',
}

export type RootStackParamList = {
  [RootScreenNames.Login]: NavigatorScreenParams<PrivateRootStackParamList>;
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
