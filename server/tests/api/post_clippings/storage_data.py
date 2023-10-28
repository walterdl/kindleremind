from pymongo import ReplaceOne
from pymongo.results import BulkWriteResult
from pytest import fixture
from unittest.mock import Mock, patch
from tests.api.common_fixtures import clippings
from kindleremind.api.post_clippings.storage import Storage


class DummyReplaceOne():
    base = ReplaceOne

    def __init__(self, filter=None, replacement=None, upsert=None):
        self.filter = filter
        self.replacement = replacement
        self.upsert = upsert


def mock_replace_one(func):
    """
    A custom decorator to mock pymongo.ReplaceOne with DummyReplaceOne.
    """
    patched_func = patch(
        'kindleremind.api.post_clippings.storage.ReplaceOne', DummyReplaceOne)(func)

    return patched_func


class DummyClippingsCollection():
    def bulk_write(self, operations, ordered=None):
        self.operations = operations
        self.ordered = ordered

        return BulkWriteResult({
            'nModified': 14,
            'nUpserted': 7,
        }, acknowledged=True)

    def executed_operations(self):
        return self.operations


@fixture()
def clippings_collections():
    collection = DummyClippingsCollection()
    mock_collection = Mock(wraps=collection)
    mock_collection.operations = []

    return mock_collection


@fixture()
def app_context():
    return {
        'email': 'The user email'
    }


@fixture()
def instance(app_context, clippings_collections):
    return Storage(app_context, clippings_collections)
