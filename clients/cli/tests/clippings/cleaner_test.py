import kindleremind.clippings.cleaner as cleaner


def test_remove_initial_white_spaces():
    line = '    hello-world'
    result = cleaner.clear_line(line)
    assert result == 'hello-world'


def test_remove_initial_break_lines():
    line = '\n\n\n\n\nhello-world'
    result = cleaner.clear_line(line)
    assert result == 'hello-world'


def test_remove_initial_boom_chars():
    line = f'{chr(65279)}{chr(65279)}{chr(65279)}hello-world'
    result = cleaner.clear_line(line)
    assert result == 'hello-world'


def test_remove_final_white_spaces():
    line = 'hello-world    '
    result = cleaner.clear_line(line)
    assert result == 'hello-world'


def test_remove_final_break_lines():
    line = 'hello-world\n\n\n\n\n'
    result = cleaner.clear_line(line)
    assert result == 'hello-world'


def test_remove_final_boom_chars():
    line = f'hello-world{chr(65279)}{chr(65279)}{chr(65279)}'
    result = cleaner.clear_line(line)
    assert result == 'hello-world'
