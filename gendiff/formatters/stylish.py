"""Stylish format."""

from gendiff.diff import ADD, IDENTICAL, NESTED, REMOVE, UPDATE

INDENT = '    '
INDENT_ADD = '  + '
INDENT_REMOVE = '  - '

QUOTE_IN = '{'
QUOTE_OUT = '}'


def format_stylish(diff: list) -> str:
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
    indent_nested = deep_indent + 1
    indent_quote = INDENT * deep_indent
    indent_mark_node = INDENT * (deep_indent - 1)

    for node in nodes:
        mark, node_key, node_value = map(node.get, ('state', 'key', 'value'))
        if mark == NESTED:
            output.append(
                format_result(indent_quote, QUOTE_IN, node_key),
            )
            output.extend(ast_walk(node.get('children'), indent_nested))
            output.append(format_result(indent_quote, QUOTE_OUT))
        elif mark == UPDATE:
            old_data = (INDENT_REMOVE, node.get('old_value'))
            new_data = (INDENT_ADD, node.get('new_value'))
            for indent, node_data in old_data, new_data:
                if isinstance(node_data, dict):
                    output.append(format_result(
                        indent_mark_node,
                        QUOTE_IN,
                        node_key,
                        indent,
                    ))
                    output.extend(format_nested(node_data, indent_nested))
                    output.append(format_result(
                        indent_quote,
                        QUOTE_OUT,
                    ))
                else:
                    output.append(format_result(
                        indent_mark_node,
                        convert(node_data),
                        node_key,
                        indent,
                    ))
        else:
            indent_mark = get_indent_by_mark(mark)
            if isinstance(node_value, dict):
                output.append(format_result(
                    indent_mark_node,
                    QUOTE_IN,
                    node_key,
                    indent_mark,
                ))
                output.extend(format_nested(node_value, indent_nested))
                output.append(format_result(
                    indent_quote,
                    QUOTE_OUT,
                ))
            else:
                output.append(format_result(
                    indent_mark_node,
                    convert(node_value),
                    node_key,
                    indent_mark,
                ))
    return output


def format_nested(node: dict, deep_indent: int) -> list:
    """
    Format nested value.

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
            output.extend(format_nested(element, deep_indent + 1))
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
    if mark == IDENTICAL:
        return INDENT
    elif mark == ADD:
        return INDENT_ADD
    elif mark == REMOVE:
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
