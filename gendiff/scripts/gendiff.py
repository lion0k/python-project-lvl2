#!/usr/bin/env python

"""Main program."""

from gendiff import generate_diff
from gendiff.cli import get_input_params


def main():
    """Start CLI-program gendiff."""
    args = get_input_params()
    diff = generate_diff(
        first_file=args['first_file'],
        second_file=args['second_file'],
        output_format=args['format'],
    )

    print(diff)


if __name__ == '__main__':
    main()
