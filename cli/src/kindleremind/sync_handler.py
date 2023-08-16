import os

from kindleremind.exceptions import AppException
import kindleremind.clippings.parser as clippings_parser


def handler(args):
    file = args.file[0]
    _check_file_existence(file)
    clippings_parser.parse(file)


def _check_file_existence(path):
    if not os.path.isfile(path):
        raise AppException('File does not exist.')
