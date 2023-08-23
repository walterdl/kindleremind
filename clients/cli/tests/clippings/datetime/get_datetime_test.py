import pytest
from datetime import datetime
import dateutil.tz as tz

from kindleremind.clippings.datetime import get_datetime


@pytest.fixture()
def metadata_and_expected_datetimes():
    return [
        (
            '- La subrayado en la posición 1181-1181 | Añadido el sábado, 17 de diciembre de 2022 2:30:30 p. m.',
            datetime(2022, 12, 17, 14, 30, 30, tzinfo=tz.tzlocal())
        ),
        (
            '- La subrayado en la página 17 | posición 204-207 | Añadido el domingo, 1 de enero de 2023 10:29:48',
            datetime(2023, 1, 1, 10, 29, 48, tzinfo=tz.tzlocal())
        ),
        (
            '- Your Highlight on page 92 | location 1406-1407 | Added on Saturday, 26 March 2016 14:59:39',
            datetime(2016, 3, 26, 14, 59, 39, tzinfo=tz.tzlocal())
        ),
        (
            '- Your Highlight at location 784-785 | Added on Saturday, 26 March 2016 11:37:26 p. m.',
            datetime(2016, 3, 26, 23, 37, 26, tzinfo=tz.tzlocal())
        )
    ]


def test_return_datetime_obj_for_given_metadata(metadata_and_expected_datetimes):
    for (metadata, expected_datetime) in metadata_and_expected_datetimes:
        assert get_datetime(metadata) == expected_datetime
