"""Generate difference."""

from gendiff.engine import converting, read_file
from gendiff.markers import MARK_ADD, MARK_IDENTICAL, MARK_REMOVE
from gendiff.views.view import view

DEFAULT_OBJECT_IN_PYTHON = (True, False, None)


def generate_diff(first_file: str, second_file: str, formatter='stylish'):
    """
    Generate difference.

    Args:
        first_file: first file
        second_file: second file
        formatter: output style view

    Returns:
        str:
    """
    old_data = read_file(first_file)
    new_data = read_file(second_file)
    diff = find_difference(old_data, new_data)
    return view(formatter)(diff)


def get_data_by_key(node_key, node):
    """
    Get data by node key.

    Args:
        node_key: possible key in node
        node: node

    Returns:
        any: value by node or None
    """
    if node_key in node:
        value_by_key = node.get(node_key)
        if value_by_key in DEFAULT_OBJECT_IN_PYTHON:
            return converting(value_by_key)
        return value_by_key


def set_marker_by_key(node_key, old_data, new_data) -> tuple:
    """
    Set data change marking.

    Args:
        node_key: key node
        old_data: data before
        new_data: new data

    Returns:
        tuple: tuple(mark changes, data)
    """
    value_old_data = get_data_by_key(node_key, old_data)
    value_new_data = get_data_by_key(node_key, new_data)
    if value_old_data == value_new_data:
        return (MARK_IDENTICAL, value_old_data),
    elif value_old_data is None:
        return (MARK_ADD, value_new_data),
    elif value_new_data is None:
        return (MARK_REMOVE, value_old_data),
    elif isinstance(value_old_data, dict) and isinstance(value_new_data, dict):
        return find_difference(value_old_data, value_new_data)
    return (MARK_REMOVE, value_old_data), (MARK_ADD, value_new_data),


def find_difference(old_data, new_data) -> dict:
    """
    Find difference and create difference structure.

    Args:
        old_data: first file
        new_data: second file

    Returns:
        dict:
    """
    diff_result = {}
    union_keys = old_data.keys() | new_data.keys()
    for key in union_keys:
        diff_result[key] = set_marker_by_key(key, old_data, new_data)
    return diff_result
