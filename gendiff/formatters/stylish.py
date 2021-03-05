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
        state = node.get('state')
        key = node.get('key')
        value = stringify(node.get('value'), depth)
        old_value = stringify(node.get('old_value'), depth)
        new_value = stringify(node.get('new_value'), depth)
        prepare_format = '{indent}{{indent_state}}{key}: {{value}}'.format(
            indent=INDENT * (depth - 1),
            key=key,
        )
        if state == NESTED:
            result.append('{indent}{key}: {{'.format(
                indent=INDENT * depth,
                key=key,
            ))
            result.extend(walk_tree(node.get('children'), depth + 1))
            result.append('{indent}}}'.format(indent=INDENT * depth))
        elif state == UPDATE:
            result.append(prepare_format.format(
                indent_state=INDENT_REMOVE,
                value=old_value,
            ))
            result.append(prepare_format.format(
                indent_state=INDENT_ADD,
                value=new_value,
            ))
        elif state == ADD:
            result.append(prepare_format.format(
                indent_state=INDENT_ADD,
                value=value,
            ))
        elif state == IDENTICAL:
            result.append(prepare_format.format(
                indent_state=INDENT,
                value=value,
            ))
        else:
            result.append(prepare_format.format(
                indent_state=INDENT_REMOVE,
                value=value,
            ))
    return result


def stringify(value, depth: int, key=None):
    """
    Output of string values.

    Args:
        value: value
        depth: count deepness indent
        key: key

    Returns:
        any:
    """
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if not isinstance(value, dict):
        return value

    result = []
    result.append('{')
    for key_item, element in value.items():
        result.append('{indent}{key}: {value}'.format(
            indent=INDENT * (depth + 1),
            key=key_item,
            value=stringify(element, depth + 1, key_item),
        ))
    result.append('{indent}}}'.format(indent=INDENT * depth))

    return '\n'.join(result)
