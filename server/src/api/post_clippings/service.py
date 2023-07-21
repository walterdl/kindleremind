import copy
from .validator import validate_clippings, is_empty_str


class WriteClippingsService:
    def __init__(self, key_generator, storage):
        self.key_generator = key_generator
        self.storage = storage

    def write(self, clippings):
        validate_clippings(clippings)
        clippings = copy.deepcopy(clippings)
        self._add_keys(clippings)
        self.storage.save(clippings)

    def _add_keys(self, clippings):
        for clipping in clippings:
            if not is_empty_str('content', clipping):
                # Even the title is included in the key when the clipping has content;
                # Book authors can coincidentally have same passages.
                clipping["key"] = self.key_generator(
                    clipping['content'] + clipping['title'])
            else:
                position = clipping['position']['location']
                if 'page' in clipping['position']:
                    position += clipping['position']['page']

                clipping['key'] = self.key_generator(
                    clipping['title'] + position)
