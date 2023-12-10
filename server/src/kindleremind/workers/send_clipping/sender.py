import json


class ClippingSender():
    def __init__(self, firebase_messaging):
        self.firebase_messaging = firebase_messaging

    def send_clipping(self, clipping, device_token):
        message = self.firebase_messaging.Message(
            token=device_token,
            data={
                'clipping': self._format_clipping(clipping)
            },
            android=self._get_android_config()
        )
        self.firebase_messaging.send(message)

    def _format_clipping(self, clipping):
        return json.dumps({
            **clipping,
            'timestamp': clipping['timestamp'].isoformat()
        })

    def _get_android_config(self):
        return self.firebase_messaging.AndroidConfig(
            priority='high',
        )
