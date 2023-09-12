export enum ScreenNames {
  Login = 'Login',
  Home = 'Home',
}

export type RootStackParamList = {
  [ScreenNames.Login]: undefined;
  [ScreenNames.Home]: undefined;
};
