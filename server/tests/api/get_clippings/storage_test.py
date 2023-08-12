import pytest
import pymongo
from .storage_data import get_storage_instance, clippings_list


def test_queries_all_clippings():
    storage = get_storage_instance()
    storage.query_clippings()
    applied_filter = storage.collection.find.mock_calls[0].args[0]

    assert applied_filter == {}


def test_formats_sorting_order():
    storage = get_storage_instance()
    storage.query_clippings(
        options={'sort': {'title': 'asc', 'author': 'desc'}})
    sort = storage.collection.find.mock_calls[0].kwargs['sort']

    assert sort == [('title', pymongo.ASCENDING),
                    ('author', pymongo.DESCENDING)]


def test_ignores_mongo_id():
    storage = get_storage_instance()
    storage.query_clippings()
    projection = storage.collection.find.mock_calls[0].kwargs['projection']

    assert projection == {'_id': False}


def test_returns_clippings_as_list():
    storage = get_storage_instance()
    result = storage.query_clippings()
    assert result == clippings_list
