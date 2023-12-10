from enum import Enum


class ClippingSenderService:
    def __init__(self, clippings_storage, tokens_storage, sender):
        self._clippings_storage = clippings_storage
        self._tokens_storage = tokens_storage
        self._sender = sender

    def send_clipping(self):
        token = self._tokens_storage.get_token()
        if not token:
            return

        clipping = self._clippings_storage.get_random_clipping()
        if not clipping:
            return

        self._sender.send_clipping(clipping, token)
