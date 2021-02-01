"""Plain format."""

from gendiff.markers import MARK_ADD, MARK_IDENTICAL

COMPLEX_VALUE = '[complex value]'
OBJECT_IN_JSON = ('true', 'false', 'null')
PROPERTY_ADDED = "Property '{}' was added with value: {}"
PROPERTY_REMOVED = "Property '{}' was removed"
PROPERTY_UPDATED = "Property '{}' was updated. From {} to {}"


def plain(diff: dict) -> str:
    """
    View style.

    Args:
        diff: difference structure

    Returns:
        str:
    """
    return '\n'.join(ast_walk(diff))


def ast_walk(node: dict, path='') -> list:
    """
    Walk to difference structure tree.

    Args:
        node: difference tree
        path: path keys

    Returns:
        list:
    """
    output = []
    for node_key, node_data in sorted(node.items()):
        if isinstance(node_data, tuple):
            mark, changes_data = node_data[0]
            if mark == MARK_IDENTICAL:
                continue
            output.append(format_result(node_key, node_data, path))
        elif isinstance(node_data, dict):
            output.extend(ast_walk(node_data, add_path(node_key, path)))
        else:
            output.append(format_result(node_key, node_data, path))
    return output


def format_result(node_key: str, node_data, path: str) -> str:
    """
    Format result.

    Args:
        node_key: name node key
        node_data: data by node_key
        path: path keys

    Returns:
        str:
    """
    added_value, removed_value = None, None
    for item_mark in node_data:
        mark, changes_data = item_mark
        if mark == MARK_ADD:
            added_value = changes_data
        else:
            removed_value = changes_data
    if added_value is not None and removed_value is not None:
        return PROPERTY_UPDATED.format(
            add_path(node_key, path),
            modify_values(removed_value),
            modify_values(added_value),
        )
    elif added_value is not None:
        return PROPERTY_ADDED.format(
            add_path(node_key, path),
            modify_values(added_value),
        )
    return PROPERTY_REMOVED.format(
        add_path(node_key, path),
        modify_values(removed_value),
    )


def add_path(node_key: str, current_path: str) -> str:
    """
    Add key in path keys.

    Args:
        node_key: name node key
        current_path: current path keys

    Returns:
        str:
    """
    if current_path:
        return '{path}.{key}'.format(path=current_path, key=node_key)
    return node_key


def modify_values(node_data) -> str:
    """
    Modify output values.

    Args:
        node_data: data

    Returns:
        str:
    """
    if is_complex(node_data):
        return COMPLEX_VALUE
    elif node_data not in OBJECT_IN_JSON and isinstance(node_data, str):
        return "'{data}'".format(data=node_data)
    return node_data


def is_complex(node_data) -> bool:
    """
    Check node is complex.

    Args:
        node_data: name node key

    Returns:
        bool:
    """
    return isinstance(node_data, dict)
