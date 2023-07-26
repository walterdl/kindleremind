from pymongo import ReplaceOne
from pytest import fixture
from unittest.mock import Mock, patch
from tests.api.common_fixtures import clippings


class DummyReplaceOne():
    base = ReplaceOne

    def __init__(self, document=None, replacement=None, upsert=None):
        self.document = document
        self.replacement = replacement
        self.upsert = upsert


def mock_replace_one(func):
    """
    A custom decorator to mock pymongo.ReplaceOne with DummyReplaceOne.
    """
    patched_func = patch(
        'api.post_clippings.storage.ReplaceOne', DummyReplaceOne)(func)

    return patched_func


class DummyClippingsCollection():
    def bulk_write(self, operations, ordered=None):
        self.operations = operations
        self.ordered = ordered

    def executed_operations(self):
        return self.operations


@fixture()
def clippings_collections():
    collection = DummyClippingsCollection()
    mock_collection = Mock(wraps=collection)
    mock_collection.operations = []

    return mock_collection
