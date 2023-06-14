import clippings.raw_abstractor as raw_abstractor
import clippings.header as header


def parse(file_path):
    skipped = 0
    raw_clippings = raw_abstractor.abstract_raw_clippings(file_path)
    for raw_clipping in raw_clippings:
        header = get_header(raw_clipping, skipped)
        print(header)


def get_header(raw_clipping, skipped):
    try:
        return header.get_header(raw_clipping[0])
    except (ValueError, IndexError):
        skipped += 1
