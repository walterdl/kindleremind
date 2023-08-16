"""Parsing module for clipping files.

This is the entry point for the clippings parsing functionality.
Given a file path to a clippings file, this module abstracts the clippings,
returning them in an array of dictionaries.
"""

import kindleremind.clippings.raw_abstractor as raw_abstractor
from kindleremind.clippings.header import parse_header
from kindleremind.clippings.metadata import parse_metadata
import kindleremind.json_printer as json_printer


def parse(file_path):
    """Parse the clippings file at the given path.

    Returns an array of dictionaries, each representing a clipping.
    Example of output:
    [
        {
            "title": "The Book Title",
            "author": "The Author",
            "type": "HIGHLIGHT", (see metadata.CLIPPING_TYPE)
            "page": "123", (None for clippings without page number)
            "location": "1234-1235",
            "date": "2019-01-01T00:00:00.000Z", (ISO 8601 format)
            "content": "The highlighted text.", (None for clippings without content)
        },
        ...
    ]
    """
    skipped = 0
    raw_clippings = raw_abstractor.abstract_raw_clippings(file_path)
    clippings = []

    for raw_clipping in raw_clippings:
        try:
            clippings.append(_parse_raw_clipping(raw_clipping))
        except Exception:
            skipped += 1

    json_printer.print({
        "clippings": clippings,
        "skipped": skipped,
    })


def _parse_raw_clipping(raw_clipping):
    return {
        **parse_header(raw_clipping[0]),
        **parse_metadata(raw_clipping[1]),
        "content": raw_clipping[2] if len(raw_clipping) > 2 else None,
    }
