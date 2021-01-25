"""Helper scripts."""

import json
from os.path import splitext


def read_file(path_to_file: str) -> dict:
    """
    Read file data.

    Args:
        path_to_file: path to file

    Returns:
         dict
    """
    file_extension = splitext(path_to_file)[1][1:]
    if file_extension == 'json':
        with open(path_to_file) as file_descriptor:
            return json.load(file_descriptor)
