"""Test diff."""

from os.path import abspath, dirname, sep

import pytest

from gendiff import generate_diff
from gendiff.gendiff import read_file

ABSOLUTE_PATH_FIXTURE_DIR = '{abs_path}{sep}{dir_fixtures}{sep}'.format(
    abs_path=abspath(dirname(__file__)),
    sep=sep,
    dir_fixtures='fixtures',
)


def get_file_absolute_path(filename: str) -> str:
    """
    Get absolute path file in directory fixtures.

    Args:
        filename: file name

    Returns:
        str:
    """
    return '{abs_path}{filename}'.format(
        abs_path=ABSOLUTE_PATH_FIXTURE_DIR,
        filename=filename,
    )


def test_file_not_found():
    """Check get exception file not found."""
    file_name = 'not_exist_file'
    with pytest.raises(FileNotFoundError) as exc:
        read_file(file_name)
        assert str(exc.value) == "File '{file}' not found!".format(
            file=file_name,
        )


def test_file_is_empty():
    """Check get exception file is empty."""
    file_name = 'empty_file'
    abs_path_to_file = get_file_absolute_path(file_name)
    with open(abs_path_to_file, 'w'):
        with pytest.raises(ValueError) as exc:
            read_file(abs_path_to_file)
            assert str(exc.value) == "'{file}' is empty!".format(
                file=abs_path_to_file,
            )


@pytest.mark.parametrize('before, after, formatter, diff', [
    ('file1.json', 'file2.json', 'stylish', 'flat_diff_result'),
    ('file1_ast.json', 'file2_ast.json', 'stylish', 'stylish_diff_result'),
    ('file1_ast.yaml', 'file2_ast.yaml', 'stylish', 'stylish_diff_result'),
    ('file1_ast.json', 'file2_ast.json', 'plain', 'plain_diff_result'),
    ('file1_ast.yaml', 'file2_ast.yaml', 'plain', 'plain_diff_result'),
    ('file1_ast.json', 'file2_ast.json', 'json', 'json_diff_result'),
    ('file1_ast.yaml', 'file2_ast.yaml', 'json', 'json_diff_result'),
    ])
def test_generate_diff(before, after, formatter, diff):
    """
    Check generate_diff.

    Args:
        before: file1
        after:  file2
        formatter: type formatter
        diff: expected result
    """
    expected = read_file(get_file_absolute_path(diff))
    assert generate_diff(
        get_file_absolute_path(before),
        get_file_absolute_path(after),
        output_format=formatter,
    ) == expected
