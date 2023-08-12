from .service_data import service, storage_clippings, storage_query_result


def test_gets_clippings_ordered_by_title(service):
    service.get_clippings()

    service.storage.query_clippings.assert_called_once_with({
        'order_by': 'title'
    })


def test_returns_what_storage_returns(service, storage_query_result):
    result = service.get_clippings()

    assert result == storage_query_result


def test_formats_dates_to_iso_format(service, storage_clippings):
    result = service.get_clippings()

    for i, clipping in enumerate(result):
        assert clipping['timestamp'] == storage_clippings[i]['iso_timestamp']
