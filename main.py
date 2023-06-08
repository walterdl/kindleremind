import argparse

import sync_handler

parser = argparse.ArgumentParser(
    description="kindleremind CLI client allows management of highlights captured on kindle devices."
)
subparser = parser.add_subparsers(
    title="subcommands",
    help="Use <command> --help for more information of the subcommand.",
    required=True,
)
syncCommand = subparser.add_parser(
    'sync',
    description="Syncs the highlights with the server.",
)
syncCommand.add_argument(
    '-f', '--file',
    help='Absolute or relative path from where the program is run to the file containing the highlights. (default: %(default)s)',
    default="./My Highlights.txt",
    required=False,
    nargs=1,
    type=str
)
syncCommand.set_defaults(handler=sync_handler.handler)

args = parser.parse_args()
args.handler(args)
