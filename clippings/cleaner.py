# 65279 = BOM (Byte Order Mark)
_empty_chars = ('\n', '\r', chr(65279), ' ')


def clear_line(line):
    return _clear_end(_clear_start(line))


def _clear_start(line):
    if line.startswith(_empty_chars):
        return _clear_start(line[1:])

    return line


def _clear_end(line):
    if line.endswith(_empty_chars):
        return _clear_end(line[:-1])

    return line
