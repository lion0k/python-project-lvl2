"""Generate difference."""

from os.path import splitext

from gendiff.diff import build_difference
from gendiff.formatter import format_diff
from gendiff.parsers import parse_data


def read_file(path_to_file):
    """
    Read file.

    Args:
        path_to_file: path to file

    Raises:
        ValueError: then file is empty or not supported
        FileNotFoundError: file not found

    Returns:
        any: data from file
    """
    with open(path_to_file) as file_descriptor:
        file_data = file_descriptor.read()
        if not file_data:
            raise ValueError("'{file}' is empty!".format(file=path_to_file))

        parse_file_data = parse_data(
            file_data,
            get_file_extension(path_to_file),
        )
        if not parse_file_data:
            raise ValueError(
                "'{file}' is not supported!".format(file=path_to_file),
            )

        return parse_file_data


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
    old_data = read_file(first_file)
    new_data = read_file(second_file)

    diff = build_difference(old_data, new_data)
    return format_diff(diff, output_format)
