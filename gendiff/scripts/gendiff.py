#!/usr/bin/env python

"""Main program."""

import argparse


def main():
    """Do main loop start the games."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', help='First file')
    parser.add_argument('second_file', help='Second file')
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
