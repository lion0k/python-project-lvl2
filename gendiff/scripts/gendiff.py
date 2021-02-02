#!/usr/bin/env python

"""Main program."""

import argparse

from gendiff import generate_diff


def main():
    """Do main loop start the games."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='First file')
    parser.add_argument('second_file', type=str, help='Second file')
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        default='stylish',
        choices=['stylish', 'plain', 'json'],
        help='set format of output (supports only stylish, plain, json)',
    )
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
