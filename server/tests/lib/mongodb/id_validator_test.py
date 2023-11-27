import pytest

from kindleremind.lib.mongodb.id_validator import validate_mongodb_id
from tests.api.common_fixtures import doc_id


@pytest.mark.parametrize(
    "id_",
    [None, 1, [], dict(), "", "Not a valid bson id"]
)
def test_return_false_for_invalid_ids(id_):
    assert validate_mongodb_id(id_) == False


def test_return_true_for_valid_ids(doc_id):
    assert validate_mongodb_id(doc_id) == True
