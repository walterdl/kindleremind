import os

from kindleremind.exceptions import AppException
import kindleremind.clippings.parser as clippings_parser
from kindleremind.print_to_file import print_to_file
from .post import send_clippings


def handler(options):
    _check_file_existence(options.file)
    result = clippings_parser.parse(options.file)
    _print_result(result, options.output)
    send_clippings(result['clippings'])


def _check_file_existence(path):
    if not os.path.isfile(path):
        raise AppException('File does not exist.')


def _print_result(result, path=None):
    print('Parsed clippings = {}\nSkipped = {}'.format(
        len(result['clippings']), result['skipped']))
    if path:
        print_to_file(result, path)
