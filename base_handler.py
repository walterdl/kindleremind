from exceptions import AppException


def handleCommand(args):
    try:
        args.handler(args)
    except Exception as e:
        printAndExit(e)


def printAndExit(error):
    if isinstance(error, AppException):
        print(error.message)
    else:
        print('Terminating program due to error.')
    exit(1)
