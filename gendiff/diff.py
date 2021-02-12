"""Difference structure."""

import json

MARK_IDENTICAL = 'identical'
MARK_ADD = 'added'
MARK_REMOVE = 'removed'


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
        if isinstance(value_by_key, bool) or value_by_key is None:
            return json.dumps(value_by_key)
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
        return build_difference(value_old_data, value_new_data)
    return (MARK_REMOVE, value_old_data), (MARK_ADD, value_new_data),


def build_difference(old_data, new_data) -> dict:
    """
    Build difference structure.

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
