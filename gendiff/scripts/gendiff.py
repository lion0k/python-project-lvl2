#!/usr/bin/env python

"""Main program."""

from gendiff import generate_diff
from gendiff.cli import get_input_params


def main():
    """Do main loop."""
    args = get_input_params()
    print(generate_diff(
        first_file=args.first_file,
        second_file=args.second_file,
        formatter=args.format,
    ))


if __name__ == '__main__':
    main()
