"""Test json files."""

from os.path import abspath, dirname, sep

from gendiff.gendiff import generate_diff

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


def test_flat_json():
    """Check flat json files."""
    with open(get_file_absolute_path('flat_diff_result')) as file_result:
        expected = file_result.read()
    assert generate_diff(
        get_file_absolute_path('file1.json'),
        get_file_absolute_path('file2.json'),
    ) == expected


def test_flat_yaml():
    """Check flat yaml files."""
    with open(get_file_absolute_path('flat_diff_result')) as file_result:
        expected = file_result.read()
    assert generate_diff(
        get_file_absolute_path('file1.yaml'),
        get_file_absolute_path('file2.yaml'),
    ) == expected