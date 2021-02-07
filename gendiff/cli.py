"""Command line interface."""

import argparse


def get_input_params():
    """
    Get input params.

    Returns:
        namespace: class Namespace with input arguments
    """
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
    return parser.parse_args()
