"""Plain format."""

from gendiff.diff import ADD, NESTED, REMOVE, UPDATE


def format_plain(diff: list) -> str:
    """
    Format to ‘plain’ style.

    Args:
        diff: difference structure

    Returns:
        str:
    """
    return '\n'.join(walk_tree(diff))


def walk_tree(nodes: list, path='') -> list:
    """
    Traverses diff tree and prepares a list of lines for output.

    Args:
        nodes: difference tree
        path: path keys

    Returns:
        list:
    """
    result = []

    for node in nodes:
        state = node.get('state')
        if state == NESTED:
            result.extend(walk_tree(
                node.get('children'),
                '{path}{key}.'.format(path=path, key=node.get('key')),
            ))
        elif state == UPDATE:
            result.append(
                "Property '{path}' was updated. From {remove} to {add}".format(
                    path='{path}{key}'.format(path=path, key=node.get('key')),
                    remove=stringify(node.get('old_value')),
                    add=stringify(node.get('new_value')),
                ),
            )
        elif state == ADD:
            result.append(
                "Property '{path}' was added with value: {add}".format(
                    path='{path}{key}'.format(path=path, key=node.get('key')),
                    add=stringify(node.get('value')),
                ),
            )
        elif state == REMOVE:
            result.append("Property '{path}' was removed".format(
                path='{path}{key}'.format(path=path, key=node.get('key')),
            ))
    return result


def stringify(value) -> str:
    """
    Prepare string representation of value.

    Args:
        value: value by node

    Returns:
        str:
    """
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return "'{value}'".format(value=value)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value
