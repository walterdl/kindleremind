/**
 * @format
 */

import {AppRegistry} from 'react-native';
import App from './src/App';
import {name as appName} from './app.json';
import {handleBackgroundNotification} from './src/core/pushNotifications';

handleBackgroundNotification();
AppRegistry.registerComponent(appName, () => App);
