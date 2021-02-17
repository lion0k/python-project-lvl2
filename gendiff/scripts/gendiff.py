#!/usr/bin/env python

"""Main program."""

from gendiff import generate_diff
from gendiff.cli import get_input_params


def main():
    """Start CLI-program gendiff."""
    first_file, second_file, formatter = get_input_params()
    diff = generate_diff(
        first_file=first_file,
        second_file=second_file,
        output_format=formatter,
    )
    print(diff)


if __name__ == '__main__':
    main()
