import React, {useCallback, useState} from 'react';
import {View} from 'react-native';
import Config from 'react-native-config';
import secureStore from 'react-native-sensitive-info';
import {Input, Button, makeStyles} from '@rneui/themed';
import type {NativeStackScreenProps} from '@react-navigation/native-stack';
import {Formik} from 'formik';
import * as yup from 'yup';

import {ScreenNames, RootStackParamList} from '../Navigation';
import {useSubmitApiKey} from './useSubmitApiKey';
import {ErrorMessage} from '../../components/ErrorMessage';

const schema = yup.object({
  apiKey: yup.string().trim().required('API Key is required'),
});

const useStyles = makeStyles(theme => ({
  errorMessage: {
    marginBottom: theme.spacing.lg,
  },
  apiKeyButton: {
    marginTop: theme.spacing.md,
  },
}));

type Props = NativeStackScreenProps<RootStackParamList, ScreenNames.Login>;

export function Authenticator(props: Props) {
  const styles = useStyles();
  const submitApiKey = useSubmitApiKey();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const submit = useCallback(
    async (apiKey: string) => {
      try {
        setLoading(true);
        setError('');
        const isValid = await submitApiKey(apiKey);

        if (isValid) {
          await secureStore.setItem('apiKey', apiKey, {});
          return props.navigation.navigate(ScreenNames.Home);
        }

        setError('Invalid API Key');
      } catch (err) {
        setError(err + '');
      } finally {
        setLoading(false);
      }
    },
    [props.navigation, submitApiKey],
  );

  const showApiKeyButton = Config.IS_DEV === 'true';

  return (
    <View>
      <Formik
        initialValues={{apiKey: ''}}
        validationSchema={schema}
        onSubmit={values => submit(values.apiKey)}>
        {form => (
          <View>
            <Input
              value={form.values.apiKey}
              placeholder="Enter API Key"
              label="API Key"
              errorMessage={form.errors.apiKey}
              onChangeText={form.handleChange('apiKey')}
              onBlur={form.handleBlur('apiKey')}
            />
            <ErrorMessage
              style={styles.errorMessage}
              message={error}
              onClose={() => setError('')}
            />
            <Button
              title="Login"
              loading={loading}
              disabled={!!form.errors.apiKey}
              onPress={() => form.handleSubmit()}
            />
            {showApiKeyButton && (
              <Button
                title="Set API Key"
                containerStyle={styles.apiKeyButton}
                type="outline"
                onPress={() =>
                  form.setValues({
                    apiKey: Config.API_KEY || '',
                  })
                }
              />
            )}
          </View>
        )}
      </Formik>
    </View>
  );
}
