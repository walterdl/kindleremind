import type {NativeStackNavigationProp} from '@react-navigation/native-stack';
import {useNavigation as useLibNavigation} from '@react-navigation/native';
import {RootStackParamList, RootScreenNames} from './types';

export function useNavigation<T extends RootScreenNames>() {
  type NavigationProp = NativeStackNavigationProp<RootStackParamList, T>;

  return useLibNavigation<NavigationProp>();
}
