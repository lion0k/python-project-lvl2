"""Stylish format."""

from gendiff.diff import (
    MARK_ADD,
    MARK_IDENTICAL,
    MARK_REMOVE,
    get_key,
    get_state_node,
    get_value,
    is_children_exist,
)

INDENT = '    '
INDENT_ADD = '  + '
INDENT_REMOVE = '  - '

QUOTE_IN = '{'
QUOTE_OUT = '}'

ALL_MARKS_WITHOUT_UPDATE = MARK_ADD, MARK_IDENTICAL, MARK_REMOVE


def stylish(diff: list) -> str:
    """
    View style.

    Args:
        diff: difference structure

    Returns:
        str:
    """
    return '{indent_start}{diff_result}{indent_finish}'.format(
        indent_start='{\n',
        diff_result='\n'.join(ast_walk(diff)),
        indent_finish='\n}',
    )


def ast_walk(nodes: list, deep_indent=1) -> list:
    """
    Walk to difference structure tree.

    Args:
        nodes: difference tree
        deep_indent: count deepness tree

    Returns:
        list:
    """
    output = []
    indent_body = deep_indent + 1
    indent_quote = INDENT * deep_indent

    for node in nodes:
        if is_children_exist(node):
            output.append(format_result(indent_quote, QUOTE_IN, get_key(node)))
            output.extend(ast_walk(node['children'], indent_body))
            output.append(format_result(indent_quote, QUOTE_OUT))
        else:
            output.extend(get_value_by_node(
                node,
                deep_indent,
                get_state_node(node),
            ))
    return output


def get_value_by_node(node: dict, deep_indent: int, mark: str) -> list:
    """
    Get value by node.

    Args:
        node: node
        deep_indent: count deep indent
        mark: special mark changes data

    Returns:
        list:
    """
    output = []

    indent_node = INDENT * (deep_indent - 1)
    indent_body = deep_indent + 1
    indent_quote_end = INDENT * deep_indent
    node_key, node_value = get_key(node), get_value(node)

    if mark in ALL_MARKS_WITHOUT_UPDATE:
        indent_mark = get_indent_by_mark(mark)
        if isinstance(node_value, dict):
            output.append(format_result(
                indent_node,
                QUOTE_IN,
                node_key,
                indent_mark,
            ))
            output.extend(format_value(node_value, indent_body))
            output.append(format_result(indent_quote_end, QUOTE_OUT))
        else:
            output.append(format_result(
                indent_node,
                convert(node_value),
                node_key,
                indent_mark,
            ))
    else:
        remove_data = (INDENT_REMOVE, node_value['remove_value'])
        add_data = (INDENT_ADD, node_value['add_value'])
        for indent, node_data in remove_data, add_data:
            if isinstance(node_data, dict):
                output.append(format_result(
                    indent_node,
                    QUOTE_IN,
                    node_key,
                    indent,
                ))
                output.extend(format_value(node_data, indent_body))
                output.append(format_result(indent_quote_end, QUOTE_OUT))
            else:
                output.append(format_result(
                    indent_node,
                    convert(node_data),
                    node_key,
                    indent,
                ))
    return output


def format_value(node: dict, deep_indent: int) -> list:
    """
    Format value.

    Args:
        node: node
        deep_indent: count deep indent

    Returns:
        list:
    """
    output = []
    for node_key, element in node.items():
        if isinstance(element, dict):
            output.append(format_result(
                INDENT * deep_indent,
                QUOTE_IN,
                node_key,
            ))
            output.extend(format_value(element, deep_indent + 1))
            output.append(format_result(INDENT * deep_indent, QUOTE_OUT))
        else:
            output.append(format_result(
                INDENT * deep_indent,
                convert(element),
                node_key,
            ))
    return output


def get_indent_by_mark(mark: str) -> str:
    """
    Get special indent by mark.

    Args:
        mark: special mark

    Returns:
        str:
    """
    if mark == MARK_IDENTICAL:
        return INDENT
    elif mark == MARK_ADD:
        return INDENT_ADD
    elif mark == MARK_REMOVE:
        return INDENT_REMOVE


def format_result(indent: str, element, node_key='', indent_mark='') -> str:
    """
    Format result.

    Args:
        indent: indent
        element: value by node or quote
        node_key: name key
        indent_mark: special indent show how data changes

    Returns:
        str:
    """
    if node_key:
        return '{indent}{indent_mark}{node_key}: {element}'.format(
            indent=indent,
            indent_mark=indent_mark,
            node_key=node_key,
            element=element,
        )
    return '{indent}{element}'.format(
        indent=indent,
        element=element,
    )


def convert(element):
    """
    Convert value.

    Args:
        element: value

    Returns:
        any:
    """
    if isinstance(element, bool):
        return str(element).lower()
    elif element is None:
        return 'null'
    return element
