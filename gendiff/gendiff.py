"""Generate difference."""

from os.path import splitext

from gendiff.diff import build_difference
from gendiff.formatter import formatter
from gendiff.parsers import parse_data


def read_file(path_to_file):
    """
    Read file.

    Args:
        path_to_file: path to file

    Raises:
        ValueError: then file is empty
        FileNotFoundError: file not found
        IOError: can`t read the file

    Returns:
        any: data from file
    """
    try:
        with open(path_to_file) as file_descriptor:
            file_data = file_descriptor.read()
            if not file_data:
                raise ValueError("'{file}' is empty!".format(file=path_to_file))
            return file_data
    except FileNotFoundError:
        raise FileNotFoundError(
            "File '{file}' not found!".format(file=path_to_file),
        )


def get_file_extension(file_name: str) -> str:
    """
    Get file extension.

    Args:
        file_name: file name

    Returns:
        str:
    """
    return splitext(file_name)[1][1:]


def generate_diff(first_file: str, second_file: str, output_format='stylish'):
    """
    Generate difference.

    Args:
        first_file: first file
        second_file: second file
        output_format: output style format

    Returns:
        str:
    """
    old_data = parse_data(
        read_file(first_file),
        get_file_extension(first_file),
    )
    new_data = parse_data(
        read_file(second_file),
        get_file_extension(second_file),
    )

    diff = build_difference(old_data, new_data)
    return formatter(output_format)(diff)
