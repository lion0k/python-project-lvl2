"""Plain format."""

from gendiff.diff import (
    MARK_ADD,
    MARK_IDENTICAL,
    MARK_UPDATE,
    get_key,
    get_state_node,
    get_value,
    is_children_exist,
)

COMPLEX_VALUE = '[complex value]'
OBJECT_IN_JSON = ('true', 'false', 'null')
PROPERTY_ADDED = "Property '{path}' was added with value: {add}"
PROPERTY_REMOVED = "Property '{path}' was removed"
PROPERTY_UPDATED = "Property '{path}' was updated. From {remove} to {add}"


def plain(diff: list) -> str:
    """
    View style.

    Args:
        diff: difference structure

    Returns:
        str:
    """
    return '\n'.join(ast_walk(diff))


def ast_walk(nodes: list, path='') -> list:
    """
    Walk to difference structure tree.

    Args:
        nodes: difference tree
        path: path keys

    Returns:
        list:
    """
    output = []
    for node in nodes:
        if is_children_exist(node):
            output.extend(ast_walk(
                node['children'],
                add_path(node['key'], path),
            ))
        else:
            mark = get_state_node(node)
            if mark != MARK_IDENTICAL:
                output.append(format_result(node, mark, path))
    return output


def format_result(node: dict, mark: str, path: str) -> str:
    """
    Format result.

    Args:
        node: name node key
        mark: special mark
        path: path keys

    Returns:
        str:
    """
    node_key, node_value = get_key(node), get_value(node)
    changes_path = add_path(node_key, path)
    if mark == MARK_UPDATE:
        return PROPERTY_UPDATED.format(
            path=changes_path,
            remove=modify_values(node_value['remove_value']),
            add=modify_values(node_value['add_value']),
        )
    elif mark == MARK_ADD:
        return PROPERTY_ADDED.format(
            path=changes_path,
            add=modify_values(node_value),
        )
    return PROPERTY_REMOVED.format(
        path=changes_path,
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


def modify_values(element) -> str:
    """
    Modify output values.

    Args:
        element: value by node

    Returns:
        str:
    """
    if is_complex(element):
        return COMPLEX_VALUE
    elif isinstance(element, str):
        return "'{data}'".format(data=element)
    elif isinstance(element, bool):
        return str(element).lower()
    elif element is None:
        return 'null'
    return element


def is_complex(node_data) -> bool:
    """
    Check node is complex.

    Args:
        node_data: name node key

    Returns:
        bool:
    """
    return isinstance(node_data, dict)
