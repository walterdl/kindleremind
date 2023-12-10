from unittest.mock import Mock
import pytest

from kindleremind.workers.send_clipping.clipping_storage import Storage
from tests.api.common_fixtures import doc_bid, doc_id, app_context


@pytest.fixture()
def instance(doc_bid, app_context):
    result_cursor = Mock()
    result_cursor.try_next.return_value = {
        '_id': doc_bid,
        'author': 'Foo Bar',
    }
    collection = Mock()
    collection.aggregate.return_value = result_cursor

    return Storage(app_context, collection)


def test_get_clipping_related_to_the_user(instance, app_context):
    instance.get_random_clipping()

    aggregate_input = instance.collection.aggregate.call_args.args[0]
    match_filter = aggregate_input[0]
    assert match_filter['$match']['user'] == app_context['email']


def test_get_only_highlights(instance):
    instance.get_random_clipping()

    aggregate_input = instance.collection.aggregate.call_args.args[0]
    match_filter = aggregate_input[0]
    assert match_filter['$match']['type'] == 'HIGHLIGHT'


def test_get_random_clipping(instance):
    instance.get_random_clipping()

    aggregate_input = instance.collection.aggregate.call_args.args[0]
    sample_filter = aggregate_input[1]
    assert sample_filter == {'$sample': {'size': 1}}


def test_return_document_with_id_formatted(instance, doc_id):
    result = instance.get_random_clipping()

    assert result['id'] == doc_id
