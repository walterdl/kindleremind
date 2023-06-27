import pytest
import locale
from datetime import datetime

from clippings.datetime import _month_number


@pytest.fixture()
def change_time_locale():
    default_time_locale = locale.getlocale(locale.LC_TIME)

    # Execute the locale change when the test request it.
    def execute(locale_name):
        locale.setlocale(locale.LC_TIME, locale_name)
    yield execute

    # Restore the default locale.
    locale.setlocale(locale.LC_TIME, default_time_locale)


@pytest.mark.parametrize(
    'locale_name',
    [
        'en_US.UTF-8',
        'es_ES.UTF-8',
    ]
)
def test_return_month_number(locale_name, change_time_locale):
    change_time_locale(locale_name)
    for (name, number) in _months():
        assert _month_number(name) == number


def _months():
    """From month numbers to month names in the current locale."""
    def name(x): return datetime.strptime(str(x), '%m').strftime('%B')

    return [(name(month_number), month_number) for month_number in range(1, 13)]


def test_try_with_hardcoded_spanish_months(change_time_locale):
    change_time_locale('en_US.UTF-8')
    assert _month_number('Mayo') == 5


def test_raise_exception_if_is_incompatible_lang():
    with pytest.raises(Exception):
        # Mei (Dutch) = May (English)
        _month_number('Mei')
