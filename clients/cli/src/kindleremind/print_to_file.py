from .clippings.json import marshall


def print_to_file(clippings, path):
    with open(path, '+w', encoding='utf-8') as results_file:
        results_file.write(marshall(clippings))
