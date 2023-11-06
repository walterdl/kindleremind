import argparse

import kindleremind.base_handler as base_handler
import kindleremind.sync_handler as sync_handler


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
    default='./My Clippings.txt',
    required=False,
    type=str,
)
syncCommand.add_argument(
    '-d', '--debug',
    help='Whether or not print error details. (default: %(default)s)',
    action='store_true',
    required=False,
)
syncCommand.add_argument(
    '-o', '--output',
    help='Absolute or relative path where the parsed clippings in JSON format should be saved.',
    required=False,
    type=str
)
syncCommand.add_argument(
    '--server-url',
    help='URL of the API.',
    required=False,
    type=str
)
syncCommand.add_argument(
    '--api-key',
    required=False,
    type=str
)

syncCommand.set_defaults(handler=sync_handler.handler)

args = parser.parse_args()
base_handler.handle_command(args)
