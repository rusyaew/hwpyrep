from argparse import ArgumentParser


def make_parser():
    parser = ArgumentParser(description='Folder navigator')
    parser.add_argument('command', metavar='CMD', type=int, choices=[1, 2, 3], help='''Command 1, 2, or 3.
    1. Output the current version of the python interpreter
    2. Create a new directory (+ additional argument --name)
    3. Print a list of files and folders of the parent directory relative to the current directory''')
    parser.add_argument('--name', type=str, help='Name argument (required if CMD is 2)')
    return parser


def validate_args(parser, args):
    if args.command == 2 and args.name is None:
        parser.error('Command 2 requires the "name" argument')
    elif args.command != 2 and args.name is not None:
        parser.error('The "name" argument can only be used with command 2.')


def __parse_args(parser):
    args = parser.parse_args()
    validate_args(parser, args)

    return args


def parse_args():
    return __parse_args(make_parser())
