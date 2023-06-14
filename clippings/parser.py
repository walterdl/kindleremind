import clippings.raw_abstractor as raw_abstractor


def parse(file_path):
    raw = raw_abstractor.abstract_raw_clippings(file_path)
    print(raw)
