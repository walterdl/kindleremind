from kindleremind.api.post_clippings.storage import Storage
from .storage_data import clippings_collections,  DummyReplaceOne, mock_replace_one, instance, app_context
from tests.api.common_fixtures import clippings


@mock_replace_one
def test_bulk_writes_without_order(instance, clippings):
    instance.save(clippings['formatted'])

    instance.collection.bulk_write.assert_called_once()
    assert instance.collection.bulk_write.call_args.kwargs['ordered'] == False


@mock_replace_one
def test_saves_clippings_in_replace_operation(instance, clippings):
    instance.save(clippings['formatted'])

    assert len(instance.collection.executed_operations()
               ) == len(clippings['formatted'])
    for operation in instance.collection.executed_operations():
        assert isinstance(operation, DummyReplaceOne)


@mock_replace_one
def test_saves_clippings_with_upsert_on(instance, clippings):
    instance.save(clippings['formatted'])

    for operation in instance.collection.executed_operations():
        assert operation.upsert == True


@mock_replace_one
def test_replaces_clippings_by_key(instance, clippings_collections, clippings):
    instance.save(clippings['formatted'])

    for i, operation in enumerate(clippings_collections.executed_operations()):
        assert operation.filter == {'key': clippings['formatted'][i]['key']}


@mock_replace_one
def test_sets_given_clipping_values(instance, clippings_collections, clippings, app_context):
    instance.save(clippings['formatted'])

    for i, operation in enumerate(clippings_collections.executed_operations()):
        assert operation.replacement == {
            **clippings['formatted'][i], 'user': app_context['email']}


@mock_replace_one
def test_returns_inserted_and_updated_clippings(instance, clippings_collections, clippings):
    result = instance.save(clippings['formatted'])

    assert result == {
        'inserted': 7,
        'updated': 14,
    }


@mock_replace_one
def test_saves_clipping_with_user_email(instance, clippings_collections, clippings, app_context):
    instance.save(clippings['formatted'])

    for i, operation in enumerate(clippings_collections.executed_operations()):
        assert operation.replacement['user'] == app_context['email']
