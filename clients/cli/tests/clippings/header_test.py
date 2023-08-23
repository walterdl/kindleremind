import pytest

from kindleremind.clippings.header import parse_header


@pytest.fixture()
def headers():
    return (
        (
            '''Refactoring: Improving the Design of Existing Code, Second Edition (Garner McCloud's Library) (Martin Fowler)''',
            {
                'title': "Refactoring: Improving the Design of Existing Code, Second Edition (Garner McCloud's Library)",
                'author': 'Martin Fowler'
            }
        ),
        (
            '''Cómo ser un estoico (Massimo Pigliucci)''',
            {
                'title': 'Cómo ser un estoico',
                'author': 'Massimo Pigliucci'
            }
        ),
        (
            '''Pragmatic Programmer, The (Thomas, David)''',
            {
                'title': 'Pragmatic Programmer, The',
                'author': 'Thomas, David'
            }
        ),
        (
            '''El coraje de ser quien eres (aunque no gustes) (Walter Riso)''',
            {
                'title': 'El coraje de ser quien eres (aunque no gustes)',
                'author': 'Walter Riso'
            }
        )
    )


def test_title(headers):
    for header, expected in headers:
        assert parse_header(header)['title'] == expected['title']


def test_author(headers):
    for header, expected in headers:
        assert parse_header(header)['author'] == expected['author']
