from parse import parse_args
from compute import print_version, create_directory, parent_directory_list

if __name__ == '__main__':
    args = parse_args()
    match args.command:
        case 1:
            print_version()
        case 2:
            create_directory(args.name)
        case 3:
            parent_directory_list()
        case _:
            exit()
