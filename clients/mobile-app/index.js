/**
 * @format
 */

import {AppRegistry} from 'react-native';
import App from './src/App';
import {name as appName} from './app.json';
import {showBackgroundPushNotification} from './src/core/pushNotifications';

showBackgroundPushNotification();
AppRegistry.registerComponent(appName, () => App);
