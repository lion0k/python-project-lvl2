"""Stylish format."""

from gendiff.diff import ADD, IDENTICAL, NESTED, UPDATE

INDENT = '    '
INDENT_ADD = '  + '
INDENT_REMOVE = '  - '


def format_stylish(diff: list) -> str:
    """
    View style.

    Args:
        diff: difference structure

    Returns:
        str:
    """
    return '{{\n{diff_result}\n}}'.format(
        diff_result='\n'.join(walk_tree(diff)),
    )


def walk_tree(nodes: list, depth=1) -> list:
    """
    Walk to difference structure tree.

    Args:
        nodes: difference tree
        depth: count deepness tree

    Returns:
        list:
    """
    result = []

    for node in nodes:
        state, key, value = map(node.get, ('state', 'key', 'value'))
        if state == NESTED:
            result.append('{indent}{key}: {{'.format(
                indent=INDENT * depth,
                key=key,
            ))
            result.extend(walk_tree(node.get('children'), depth + 1))
            result.append('{indent}}}'.format(indent=INDENT * depth))
        elif state == UPDATE:
            result.extend(format_result(
                key,
                node.get('old_value'),
                depth,
                INDENT_REMOVE,
            ))
            result.extend(format_result(
                key,
                node.get('new_value'),
                depth,
                INDENT_ADD,
            ))
        elif state == ADD:
            result.extend(format_result(key, value, depth, INDENT_ADD))
        elif state == IDENTICAL:
            result.extend(format_result(key, value, depth, INDENT))
        else:
            result.extend(format_result(key, value, depth, INDENT_REMOVE))
    return result


def format_result(key, value, depth: int, indent_state=None) -> list:
    """
    Format result.

    Args:
        key: node key
        value: node value
        depth: depth
        indent_state: special indent show how data changes

    Returns:
        list:
    """
    result = []
    if indent_state:
        if isinstance(value, dict):
            result.append('{indent}{indent_state}{key}: {{'.format(
                indent=INDENT * (depth - 1),
                indent_state=indent_state,
                key=key,
            ))
            result.extend(format_result(key, value, depth + 1))
            result.append('{indent}}}'.format(indent=INDENT * depth))
        else:
            result.append('{indent}{indent_state}{key}: {value}'.format(
                indent=INDENT * (depth - 1),
                indent_state=indent_state,
                key=key,
                value=replacer(value),
            ))
    else:
        for key_item, element in value.items():
            if isinstance(element, dict):
                result.append('{indent}{key}: {{'.format(
                    indent=INDENT * depth,
                    key=key_item,
                ))
                result.extend(format_result(key_item, element, depth + 1))
                result.append('{indent}}}'.format(indent=INDENT * depth))
            else:
                result.append('{indent}{key}: {element}'.format(
                    indent=INDENT * depth,
                    key=key_item,
                    element=replacer(element),
                ))
    return result


def replacer(value):
    """
    Replace output values.

    Args:
        value: value

    Returns:
        any:
    """
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return value
