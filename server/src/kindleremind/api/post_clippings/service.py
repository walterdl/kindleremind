import copy
from .validator import validate_clippings
from .dates import iso_to_utc_datetime


class WriteClippingsService:
    def __init__(self, key_generator, storage):
        self.key_generator = key_generator
        self.storage = storage

    def write(self, clippings):
        validate_clippings(clippings)
        clippings = copy.deepcopy(clippings)
        self._add_keys(clippings)
        self._timestamps_to_utc_datetime(clippings)
        self.storage.save(clippings)

    def _add_keys(self, clippings):
        for clipping in clippings:
            clipping['key'] = self.key_generator.generate_key(clipping)

    def _timestamps_to_utc_datetime(self, clippings):
        for clipping in clippings:
            clipping['timestamp'] = iso_to_utc_datetime(clipping['timestamp'])
