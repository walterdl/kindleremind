import copy
import pytest
from bson.objectid import ObjectId


@pytest.fixture()
def clippings():
    base1 = {
        "author": "Martin Fowler",
        "content": "Brevity is the soul of wit,",
        "position": {
            "location": "1181-1181",
            "page": "83"
        },
        "timestamp": "2022-12-17T14:30:30-05:00",
        "title": "Refactoring: Improving the Design of Existing Code, Second Edition (Garner McCloud's Library)",
        "type": "HIGHLIGHT"
    }
    base2 = {
        "author": "Walter Riso",
        "content": "El punto de control interno: Sobre mí decido yo",
        "position": {
            "location": "646-648"
        },
        "timestamp": "2023-01-07T22:56:48-05:00",
        "title": "El coraje de ser quien eres (aunque no gustes)",
        "type": "HIGHLIGHT"
    }

    return copy.deepcopy({
        "base": [base1, base2],
        "formatted": [
            {**base1, 'key': '1'},
            {**base2, 'key': '2'},
        ]
    })


@pytest.fixture()
def app_context():
    return {
        'email': 'user@email.com'
    }


@pytest.fixture()
def doc_id():
    """A valid ObjectId (BSON) string."""
    return '6545cb6f1abf8bf1274d6e2f'


@pytest.fixture()
def doc_bid(doc_id):
    """ObjectId (BSON) representation of the doc_id fixture."""
    return ObjectId(doc_id)
