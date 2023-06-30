
import pytest


_valid_inputs = (
    {
        "author": "Martin Fowler",
        "content": "Brevity is the soul of wit,",
        "position": {
            "location": "1181-1181"
        },
        "timestamp": "2022-12-17T14:30:30-05:00",
        "title": "Refactoring: Improving the Design of Existing Code, Second Edition (Garner McCloud's Library)",
        "type": "HIGHLIGHT"
    },
    {
        "author": "Pigliucci, Massimo",
        "content": "Para un estoico, en última instancia no importa si creemos que el Logos es Dios o la naturaleza, siempre que reconozcamos que una vida humana digna se tiene que centrar en el cultivo del car\u00e1cter personal y en la preocupaci\u00f3n por las dem\u00e1s personas (e incluso por la propia naturaleza), y que se disfruta m\u00e1s si se adopta un camino adecuado \u2014pero no fan\u00e1tico\u2014 para distanciarse de los bienes puramente mundanos.",
        "position": {
            "location": "204-207",
            "page": "17"
        },
        "timestamp": "2023-01-01T22:29:48-05:00",
        "title": "Cómo ser un estoico (Ariel) (Spanish Edition)",
        "type": "HIGHLIGHT"
    }
)
_invalid_positions = (
    {
        **_valid_inputs[0],
        "position": None
    },
    {
        **_valid_inputs[0],
        "position": {}
    },
    {
        **_valid_inputs[0],
        "position": {}
    },
    {
        **_valid_inputs[0],
        "position": {
            "location": None
        }
    },
    {
        **_valid_inputs[0],
        "position": {
            "location": "xyz",
            "page": None
        }
    }
)


@pytest.fixture()
def valid_inputs():
    return _valid_inputs


@pytest.fixture()
def invalid_inputs():
    invalid_values = (None, "", 123, [], True)
    fields = (
        'author',
        'position',
        'timestamp',
        'title',
        'type',
    )
    # Pre-populate with invalid clippings.
    result = [None, 123, True, ""]

    for invalid_value in invalid_values:
        for field in fields:
            result.append([
                {
                    # Just grab the first valid input.
                    **_valid_inputs[0],
                    field: invalid_value
                }
            ])
    result.extend(_invalid_positions)

    return result


@pytest.fixture()
def invalid_collections():
    return (
        None,
        {},
        123,
        True,
        ""
    )
