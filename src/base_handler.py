from exceptions import AppException


def handleCommand(args):
    try:
        args.handler(args)
    except Exception as e:
        printAndExit(e, args.debug)


def printAndExit(error, debug=False):
    if isinstance(error, AppException):
        print(error if debug else error.message)
    else:
        print(error if debug else 'Terminating program due to error.')
    exit(1)
