import clippings.raw_abstractor as raw_abstractor
import clippings.header as header
import clippings.metadata as metadata
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
        "header": header.get_header(raw_clipping[0]),
        "metadata": metadata.get_metadata(raw_clipping[1]),
    }
