import pytest
import pymongo
from .storage_data import instance, clippings_list, app_context


def test_queries_all_clippings_of_the_user(instance, app_context):
    instance.query_clippings()
    applied_filter = instance.collection.find.mock_calls[0].args[0]

    assert applied_filter == {'user': app_context['email']}


def test_formats_sorting_order(instance):
    instance.query_clippings(
        options={'sort': {'title': 'asc', 'author': 'desc'}})
    sort = instance.collection.find.mock_calls[0].kwargs['sort']

    assert sort == [('title', pymongo.ASCENDING),
                    ('author', pymongo.DESCENDING)]


def test_ignores_mongo_id(instance):
    instance.query_clippings()
    projection = instance.collection.find.mock_calls[0].kwargs['projection']

    assert projection == {'_id': False}


def test_returns_clippings_as_list(instance):
    result = instance.query_clippings()
    assert result == clippings_list
