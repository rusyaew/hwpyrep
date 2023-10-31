import os
import sys


def print_version():
    print(sys.version)


def create_directory(name):
    try:
        os.mkdir(name)
        print(f"Directory '{name}' created.")
    except FileExistsError:
        print(f"Directory '{name}' already exists.")


def parent_directory_list():
    for element in os.listdir(os.path.abspath('..')):
        print(element)
