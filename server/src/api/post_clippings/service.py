from .validator import validate_clippings


class WriteClippingsService:
    def write(self, clippings):
        validate_clippings(clippings)
