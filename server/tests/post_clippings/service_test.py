import pytest
from unittest.mock import Mock
from api.post_clippings.service import WriteClippingsService
from .service_data import get_write_clippings_service, valid_clippings, invalid_inputs, invalid_collections


def test_throw_validation_exception_for_invalid_collections(invalid_collections):
    for input in invalid_collections:
        service = get_write_clippings_service()
        with pytest.raises(ValueError) as error:
            service.write(input)
        error.match("Expected a list of clippings")


def test_throw_validation_exception_for_invalid_clippings(invalid_inputs):
    for input in invalid_inputs:
        service = get_write_clippings_service()

        try:
            service.write(input)
            raise AssertionError(f'Expected a ValueError for: {input}')
        except ValueError:
            pass
