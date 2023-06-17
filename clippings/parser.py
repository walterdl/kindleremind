import clippings.raw_abstractor as raw_abstractor
from clippings.header import get_header
from clippings.metadata import get_metadata
import json_printer


def parse(file_path):
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
        **get_header(raw_clipping[0]),
        **get_metadata(raw_clipping[1]),
        "content": raw_clipping[2] if len(raw_clipping) > 2 else None,
    }
