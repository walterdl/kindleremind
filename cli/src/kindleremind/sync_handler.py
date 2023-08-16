import os

from kindleremind.exceptions import AppException
import kindleremind.clippings.parser as clippings_parser
from kindleremind.print_to_file import print_to_file


def handler(args):
    file = args.file[0]
    _check_file_existence(file)
    result = clippings_parser.parse(file)
    _print_result(result)


def _check_file_existence(path):
    if not os.path.isfile(path):
        raise AppException('File does not exist.')


def _print_result(result):
    print('Parsed clippings = {}\nSkipped = {}'.format(
        len(result['clippings']), result['skipped']))
    print_to_file.print_to_file(result)
