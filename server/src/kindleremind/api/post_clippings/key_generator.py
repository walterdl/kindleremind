from .validator import is_empty_str


class ClippingKeyGenerator():
    def __init__(self, hash_function):
        self.hash_function = hash_function

    def generate_key(self, clipping):
        if not is_empty_str('content', clipping):
            # The tille is included in the key despite having content because
            # book authors could coincidentally have same passages.
            return self.hash_function(
                clipping['content'] + clipping['title'])
        else:
            position = clipping['position']['location']
            if 'page' in clipping['position']:
                position += clipping['position']['page']

            return self.hash_function(
                clipping['title'] + position)
