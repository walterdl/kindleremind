from datetime import datetime
import pytest
from .service_data import get_write_clippings_service, valid_clipping, invalid_inputs, invalid_collections


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


def test_key_for_clipping_with_content(valid_clipping):
    service = get_write_clippings_service()
    service.write([valid_clipping])
    service.key_generator.assert_called_with(
        valid_clipping['content'] + valid_clipping['title'])


def test_key_for_clipping_without_content_but_with_location(valid_clipping):
    without_content = [
        {
            **valid_clipping,
            'content': None,
            'position': {'location': '123'}
        },
        {
            **valid_clipping,
            'content': '',
            'position': {'location': '123'}
        },
    ]

    for clipping in without_content:
        service = get_write_clippings_service()
        service.write([clipping])
        service.key_generator.assert_called_once_with(
            clipping['title'] + clipping['position']['location']
        )


def test_key_for_clipping_without_content_but_with_location_and_page(valid_clipping):
    clipping = {
        **valid_clipping,
        'content': None,
        'position': {'location': '123', 'page': '456'}
    }
    service = get_write_clippings_service()
    service.write([clipping])
    position = clipping['position']['location'] + clipping['position']['page']
    service.key_generator.assert_called_once_with(
        clipping['title'] + position
    )


def test_save_clippings_with_utc_datetimes(valid_clipping):
    service = get_write_clippings_service()
    service.write([valid_clipping])
    saved_clippings = service.storage.save.call_args[0][0]

    assert isinstance(saved_clippings[0]['timestamp'], datetime)


def test_save_clippings_with_keys(valid_clipping):
    service = get_write_clippings_service()
    service.write([valid_clipping])
    saved_clippings = service.storage.save.call_args[0][0]

    assert 'key' in saved_clippings[0]
