"""Generate difference."""

from gendiff.engine import read_file

INDENT_NOT_CHANGE = '    '
INDENT_ADD = '  + '
INDENT_REMOVE = '  - '


def format_result(indent: str, key, data_by_key) -> str:
    """
    Format result.

    Args:
        indent: indent
        key: key
        data_by_key: data by key

    Returns:
         str
    """
    return '{indent}{key}: {value}'.format(
        indent=indent,
        key=str(key),
        value=str(data_by_key),
    )


def get_changes_by_key(key, data1: dict, data2: dict) -> list:
    """
    Get data changes by key.

    Args:
        key: data search by key
        data1: data for comparison
        data2: data for comparison

    Returns:
         list:
    """
    changes = []
    value_data1 = data1.get(key, None)
    value_data2 = data2.get(key, None)
    if (key in data1) and (key in data2):
        if value_data1 == value_data2:
            changes.append(format_result(INDENT_NOT_CHANGE, key, value_data1))
        else:
            changes.append(format_result(INDENT_REMOVE, key, value_data1))
            changes.append(format_result(INDENT_ADD, key, value_data2))
    elif key in data2:
        changes.append(format_result(INDENT_ADD, key, value_data2))
    else:
        changes.append(format_result(INDENT_REMOVE, key, value_data1))
    return changes


def generate_diff(first_file: str, second_file: str) -> str:
    """
    Generate difference.

    Args:
        first_file: first file
        second_file: second file

    Returns:
         str:
    """
    file1 = read_file(first_file)
    file2 = read_file(second_file)

    union_keys = set(file1.keys())
    union_keys.update(file2.keys())

    diff_result = []
    for key in sorted(union_keys):
        diff_result.extend(get_changes_by_key(key, file1, file2))

    return '{indent_start}{diff_result}{indent_finish}'.format(
        indent_start='{\n',
        diff_result='\n'.join(diff_result),
        indent_finish='\n}',
    )
