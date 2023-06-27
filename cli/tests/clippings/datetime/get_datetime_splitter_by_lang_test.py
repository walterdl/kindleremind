from clippings.datetime import _get_datetime_splitter_by_lang, _split_es_datetime, _split_en_datetime


def test_provide_the_correct_spanish_splitter():
    splitter = _get_datetime_splitter_by_lang(
        'Añadido el 17 de diciembre de 2022 3:28:17 p. m.')
    assert splitter == _split_es_datetime


def test_provide_the_correct_english_splitter():
    splitter = _get_datetime_splitter_by_lang(
        'Any other text that is not spanish')
    assert splitter == _split_en_datetime
