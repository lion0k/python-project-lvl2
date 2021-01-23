#!/usr/bin/env python

"""Main program."""

import argparse

from gendiff.gendiff import generate_diff


def main():
    """Do main loop start the games."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='First file')
    parser.add_argument('second_file', type=str, help='Second file')
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        help='set format of output',
    )
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
