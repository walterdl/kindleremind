import sys
import clippings.metadata as metadata


def test_hello():
    print('The sys.path', sys.path)
    print(metadata._BOOKMARK_TEXT)
    assert (1, 2) == (1, 2)
