class ClippingSenderService:
    def __init__(self, clippings_storage, tokens_storage, senders_by_proto):
        self._clippings_storage = clippings_storage
        self._tokens_storage = tokens_storage
        self._senders_by_proto = senders_by_proto

    def send_clipping(self):
        token = self._tokens_storage.get_token()
        if not token:
            return

        sender = self._senders_by_proto.get(token['proto'], None)
        if not sender:
            raise Exception(f"No sender for token proto {token['proto']}")

        clipping = self._clippings_storage.get_random_clipping()
        if not clipping:
            return

        sender.send_clipping({
            'token': token,
            'clipping': clipping
        })
