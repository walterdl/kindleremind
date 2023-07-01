import copy
from .validator import validate_clippings


class WriteClippingsService:
    def __init__(self, *, key_generator):
        self.key_generator = key_generator

    def write(self, clippings):
        validate_clippings(clippings)
