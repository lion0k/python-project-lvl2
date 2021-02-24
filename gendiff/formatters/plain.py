"""Plain format."""

from gendiff.diff import ADD, IDENTICAL, UPDATE


def format_plain(diff: list) -> str:
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
        changes_path = add_path(node.get('key'), path)
        if 'children' in node:
            output.extend(ast_walk(
                node.get('children'),
                changes_path,
            ))
        else:
            mark = node.get('state')
            if mark != IDENTICAL:
                if mark == UPDATE:
                    output.append(
                        "Property '{path}' was updated. From {remove} to {add}".format(
                            path=changes_path,
                            remove=modify_values(node.get('old_value')),
                            add=modify_values(node.get('new_value')),
                        ),
                    )
                elif mark == ADD:
                    output.append(
                        "Property '{path}' was added with value: {add}".format(
                            path=changes_path,
                            add=modify_values(node.get('value')),
                        ),
                    )
                else:
                    output.append("Property '{path}' was removed".format(
                        path=changes_path,
                    ))
    return output


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
    if isinstance(element, dict):
        return '[complex value]'
    elif isinstance(element, str):
        return "'{data}'".format(data=element)
    elif isinstance(element, bool):
        return str(element).lower()
    elif element is None:
        return 'null'
    return element
