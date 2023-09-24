import {TextFieldOptionsType} from '@aws-amplify/ui-react-native/dist/Authenticator/hooks';

export const signUpFields: TextFieldOptionsType[] = [
  {
    label: 'First Name',
    name: 'given_name',
    placeholder: 'Enter your First Name',
    required: true,
    type: 'default',
  },
  {
    label: 'Email',
    name: 'email',
    placeholder: 'Enter your Email',
    required: true,
    type: 'email',
  },
  {
    label: 'Password',
    name: 'password',
    placeholder: 'Enter your Password',
    required: true,
    type: 'password',
  },
  {
    label: 'Confirm Password',
    name: 'confirm_password',
    placeholder: 'Please confirm your Password',
    required: true,
    type: 'password',
  },
];
