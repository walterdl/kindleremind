import pytest
from api.post_clippings.service import WriteClippingsService
from .service_data import valid_inputs, invalid_inputs, invalid_collections


def test_throw_validation_exception_for_invalid_collections(invalid_collections):
    for input in invalid_collections:
        service = WriteClippingsService()
        with pytest.raises(ValueError) as error:
            service.write(input)
        error.match("Expected a list of clippings")


def test_throw_validation_exception_for_invalid_clippings(invalid_inputs):
    for input in invalid_inputs:
        service = WriteClippingsService()

        try:
            service.write(input)
            raise AssertionError(f'Expected a ValueError for: {input}')
        except ValueError:
            pass
