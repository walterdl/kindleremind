from api.post_clippings.storage import Storage
from .storage_data import clippings_collections,  DummyReplaceOne, mock_replace_one
from tests.api.common_fixtures import clippings
import pytest


@mock_replace_one
def test_bulk_writes_without_order(clippings_collections, clippings):
    storage = Storage(clippings_collections)

    storage.save(clippings['formatted'])

    storage.collection.bulk_write.assert_called_once()
    assert storage.collection.bulk_write.call_args.kwargs['ordered'] == False


@mock_replace_one
def test_saves_clippings_in_replace_operation(clippings_collections, clippings):
    storage = Storage(clippings_collections)

    storage.save(clippings['formatted'])

    assert len(storage.collection.executed_operations()
               ) == len(clippings['formatted'])
    for operation in storage.collection.executed_operations():
        assert isinstance(operation, DummyReplaceOne)


@pytest.mark.skip(reason='TODO')
def test_filters_clippings_by_key():
    pass


@pytest.mark.skip(reason='TODO')
def test_sets_given_clipping_values():
    pass


@pytest.mark.skip(reason='TODO')
def test_returns_inserted_and_updated_clippings():
    pass
