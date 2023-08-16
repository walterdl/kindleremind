from kindleremind.exceptions import AppException


def handle_command(args):
    try:
        args.handler(args)
    except Exception as e:
        print_and_exit(e, args.debug)


def print_and_exit(error, debug=False):
    if isinstance(error, AppException):
        print(error if debug else error.message)
    else:
        print(error if debug else 'Terminating program due to error.')
    exit(1)
