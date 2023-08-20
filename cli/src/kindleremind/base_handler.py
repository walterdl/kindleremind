from .config import init_config
from kindleremind.exceptions import AppException


def handle_command(args):
    try:
        init_config(args.__dict__)
        args.handler(args)
    except Exception as error:
        print_and_exit(error, args.debug)


def print_and_exit(error, debug=False):
    if debug:
        raise error

    if isinstance(error, AppException):
        print(error.message)
    else:
        print('Terminating program due to error.')

    exit(1)
