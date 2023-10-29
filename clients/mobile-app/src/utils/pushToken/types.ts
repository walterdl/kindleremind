export type PushTokenCallback = (token: string, proto: PushTokenProto) => void;
export type UseInitialPushToken = (receivePushToken: PushTokenCallback) => void;
export type UsePushTokenChanges = (receivePushToken: PushTokenCallback) => void;
export enum PushTokenProto {
  FCM = 'FCM',
  HMS = 'HMS',
}
