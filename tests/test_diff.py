"""Test json files."""

from os.path import abspath, dirname, sep

from gendiff import gendiff

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


def test_stylish_format_flat_files():
    """Check flat json/yaml files."""
    with open(get_file_absolute_path('flat_diff_result')) as file_result:
        expected = file_result.read()
    assert gendiff.generate_diff(
        get_file_absolute_path('file1.json'),
        get_file_absolute_path('file2.json'),
        formatter='stylish'
    ) == expected
    assert gendiff.generate_diff(
        get_file_absolute_path('file1.yaml'),
        get_file_absolute_path('file2.yaml'),
        formatter='stylish'
    ) == expected


def test_stylish_format_ast_files():
    """Check stylish format json/yaml files."""
    with open(get_file_absolute_path('stylish_diff_result')) as file_result:
        expected = file_result.read()
    assert gendiff.generate_diff(
        get_file_absolute_path('file1_ast.json'),
        get_file_absolute_path('file2_ast.json'),
        formatter='stylish'
    ) == expected
    assert gendiff.generate_diff(
        get_file_absolute_path('file1_ast.yaml'),
        get_file_absolute_path('file2_ast.yaml'),
        formatter='stylish'
    ) == expected


def test_plain_format_ast_files():
    """Check plain format json/yaml files."""
    with open(get_file_absolute_path('plain_diff_result')) as file_result:
        expected = file_result.read()
    assert gendiff.generate_diff(
        get_file_absolute_path('file1_ast.json'),
        get_file_absolute_path('file2_ast.json'),
        formatter='plain',
    ) == expected
    assert gendiff.generate_diff(
        get_file_absolute_path('file1_ast.yaml'),
        get_file_absolute_path('file2_ast.yaml'),
        formatter='plain',
    ) == expected


def test_json_format_ast_files():
    """Check json format json/yaml files."""
    with open(get_file_absolute_path('json_diff_result')) as file_result:
        expected = file_result.read()
    assert gendiff.generate_diff(
        get_file_absolute_path('file1_ast.json'),
        get_file_absolute_path('file2_ast.json'),
        formatter='json',
    ) == expected
    assert gendiff.generate_diff(
        get_file_absolute_path('file1_ast.yaml'),
        get_file_absolute_path('file2_ast.yaml'),
        formatter='json',
    ) == expected
