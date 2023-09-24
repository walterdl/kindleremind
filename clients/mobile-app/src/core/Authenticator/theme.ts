import merge from 'lodash.merge';
import {Theme, defaultDarkModeOverride} from '@aws-amplify/ui-react-native';
import {Override} from '@aws-amplify/ui-react-native/dist/theme';

const customOverride: Override = {
  colorMode: 'dark',
  tokens: {
    colors: {
      background: {
        primary: '#3f3f3f',
      },
      brand: {
        primary: {
          '10': '#00201e',
          '20': '#003734',
          '40': '#006a64',
          '60': '#00a29a',
          '80': '#4fdbd1',
          '90': '#71f7ed',
          '100': '#ffffff',
        },
      },
    },
  },
};

const customDarkMode = merge(
  // Deep clone to avoid mutating original defaultDarkModeOverride
  JSON.parse(JSON.stringify(defaultDarkModeOverride)),
  customOverride,
);

export const theme: Theme = {
  components: {
    button: {
      containerPrimary: {
        backgroundColor: '#80CBC4',
      },
      textPrimary: {
        color: 'white',
      },
    },
  },
  overrides: [customDarkMode],
};
