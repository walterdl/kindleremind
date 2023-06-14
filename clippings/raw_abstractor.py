import clippings.cleaner as cleaner


def abstract_raw_clippings(file_path):
    result = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        _process_clippings(file, result)
    return result


def _process_clippings(file, result):
    clipping = []
    for line in file:
        if is_separator(line):
            _add_clipping_if_nonempty(clipping, result)
            # Resets the raw clipping accumulator to start a new one.
            clipping = []
        else:
            _add_line_if_nonempty(line, clipping)
    else:
        # Appends the last clipping if the file does not end with a clipping separator.
        _add_clipping_if_nonempty(clipping, result)
    return result


_CLIPPING_SEPARATOR = '=========='


def is_separator(line):
    return cleaner.clear_line(line) == _CLIPPING_SEPARATOR


def _add_clipping_if_nonempty(clipping, result):
    if clipping:
        result.append(clipping)


def _add_line_if_nonempty(line, clipping):
    if cleaner.clear_line(line):
        clipping.append(cleaner.clear_line(line))
