from .key_generator_data import key_generator, clippings_without_content, no_content_but_location_and_page
from tests.api.common_fixtures import clippings


def test_key_for_clipping_with_content(key_generator, clippings):
    clipping = clippings['base'][0]
    key_generator.generate_key(clipping)
    key_generator.hash_function.assert_called_with(
        clipping['content'] + clipping['title'])


def test_key_for_clipping_without_content_but_with_location(key_generator, clippings_without_content):
    for clipping in clippings_without_content:
        key_generator.generate_key(clipping)
        key_generator.hash_function.assert_called_once_with(
            clipping['title'] + clipping['position']['location']
        )
        key_generator.hash_function.reset_mock()


def test_key_for_clipping_without_content_but_with_location_and_page(key_generator, no_content_but_location_and_page):
    clipping = no_content_but_location_and_page
    key_generator.generate_key(clipping)
    position = clipping['position']['location'] + clipping['position']['page']
    key_generator.hash_function.assert_called_once_with(
        clipping['title'] + position
    )
