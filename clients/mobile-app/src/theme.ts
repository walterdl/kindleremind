import {useMemo} from 'react';
import {Theme} from '@react-navigation/native';
import {createTheme, useTheme} from '@rneui/themed';

export const initialTheme = createTheme({
  darkColors: {
    background: '#2b2b2b',
  },
  mode: 'dark',
});

export function useNavigationTheme() {
  const {theme} = useTheme();

  return useMemo<Theme>(
    () => ({
      colors: {
        primary: theme.colors.primary,
        background: '#484848',
        card: theme.colors.background,
        text: theme.colors.black,
        border: theme.colors.grey5,
        notification: theme.colors.primary,
      },
      dark: true,
    }),
    [
      theme.colors.background,
      theme.colors.black,
      theme.colors.grey5,
      theme.colors.primary,
    ],
  );
}
