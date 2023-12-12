import pytest
from kindleremind.clippings.datetime import _split_es_datetime, _split_en_datetime


@pytest.fixture()
def spanish_datetime_in_12_hours():
    return ["17 de diciembre de 2022 3:28:17 p. m."]


@pytest.fixture()
def spanish_datetime_in_24_hours():
    return ["17 de diciembre de 2022 3:28:17"]


@pytest.fixture()
def english_datetime_in_12_hours():
    return ["26 March 2016 2:59:39 p. m."]


@pytest.fixture()
def english_datetime_in_24_hours():
    return ["26 March 2016 2:59:39"]


@pytest.fixture()
def english_datetime_in_12_hours_variant_2():
    return ["December 01", "2023 9:02:48 PM"]


def test_split_spanish_datetime_text_with_meridiem_indicator(spanish_datetime_in_12_hours):
    result = _split_es_datetime(spanish_datetime_in_12_hours)

    assert result == {
        "year": "2022",
        "month_name": "diciembre",
        "day": "17",
        "hour": "3",
        "minutes": "28",
        "seconds": "17",
        "meridiem_indicator": "p.",
    }


def test_split_spanish_datetime_text_without_meridiem_indicator(spanish_datetime_in_24_hours):
    result = _split_es_datetime(spanish_datetime_in_24_hours)

    assert result == {
        "year": "2022",
        "month_name": "diciembre",
        "day": "17",
        "hour": "3",
        "minutes": "28",
        "seconds": "17",
        "meridiem_indicator": None,
    }


def test_split_english_datetime_text_with_meridiem_indicator(english_datetime_in_12_hours):
    result = _split_en_datetime(english_datetime_in_12_hours)

    assert result == {
        "year": "2016",
        "month_name": "March",
        "day": "26",
        "hour": "2",
        "minutes": "59",
        "seconds": "39",
        "meridiem_indicator": "p.",
    }


def test_split_english_datetime_text_without_meridiem_indicator(english_datetime_in_24_hours):
    result = _split_en_datetime(english_datetime_in_24_hours)

    assert result == {
        "year": "2016",
        "month_name": "March",
        "day": "26",
        "hour": "2",
        "minutes": "59",
        "seconds": "39",
        "meridiem_indicator": None,
    }


def test_split_english_datetime_variant_2_with_meridiem_indicator(english_datetime_in_12_hours_variant_2):
    result = _split_en_datetime(english_datetime_in_12_hours_variant_2)

    assert result == {
        "year": "2023",
        "month_name": "December",
        "day": "01",
        "hour": "9",
        "minutes": "02",
        "seconds": "48",
        "meridiem_indicator": "p.",
    }
