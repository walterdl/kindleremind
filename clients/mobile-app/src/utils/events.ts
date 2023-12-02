const buildEventEmitter = require('event-emitter');

export enum Event {
  ON_BACKGROUND_PUSH_NOTIFICATION = 'ON_BACKGROUND_PUSH_NOTIFICATION',
}

const eventEmitter = buildEventEmitter();

export function emitEvent(event: Event, payload: unknown) {
  eventEmitter.emit(event, payload);
}

export function addEventListener<T>(
  event: Event,
  callback: (payload: T) => void,
) {
  eventEmitter.on(event, callback);
}

export function removeEventListener<T>(
  event: Event,
  callback: (payload: T) => void,
) {
  eventEmitter.off(event, callback);
}
