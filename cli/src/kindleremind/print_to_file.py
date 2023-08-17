from .clippings.json import marshall


def print_to_file(clippings):
    with open('data/result.json', '+w', encoding='utf-8') as results_file:
        results_file.write(marshall(clippings))
