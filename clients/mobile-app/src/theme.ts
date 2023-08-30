import {useMemo} from 'react';
import {Theme} from '@react-navigation/native';
import {createTheme, useTheme} from '@rneui/themed';

export const initialTheme = createTheme({
  darkColors: {
    background: '#2b2b2b',
    grey5: '#6b7075',
    grey4: '#93999e',
    grey3: '#b3b9bd',
    grey2: '#d6dce1',
    grey1: '#e5ebf1',
    grey0: '#eef4f9',
    error: '#ec4631',
  },
  mode: 'dark',
});

export function useNavigationTheme() {
  const {theme} = useTheme();

  return useMemo<Theme>(
    () => ({
      colors: {
        primary: theme.colors.primary,
        background: '#3f3f3f',
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
