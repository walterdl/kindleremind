import React, {useCallback, useState} from 'react';
import {View} from 'react-native';
import {Input, Button, makeStyles} from '@rneui/themed';
import {Formik} from 'formik';
import * as yup from 'yup';
import {useSubmitApiKey} from './useSubmitApiKey';
import {ErrorMessage} from '../components/ErrorMessage';

const schema = yup.object({
  apiKey: yup.string().trim().required('API Key is required'),
});

const useStyles = makeStyles(theme => ({
  errorMessage: {
    marginBottom: theme.spacing.lg,
  },
}));

export function Authenticator() {
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
          // TODO: navigate to home screen.
        }

        setError('Invalid API Key');
      } catch (err) {
        setError(err + '');
      } finally {
        setLoading(false);
      }
    },
    [submitApiKey],
  );

  const styles = useStyles();

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
          </View>
        )}
      </Formik>
    </View>
  );
}
