"""Stylish format."""

from gendiff.diff import MARK_ADD, MARK_IDENTICAL, MARK_REMOVE

INDENT = '    '
INDENT_NOT_CHANGE = '    '
INDENT_ADD = '  + '
INDENT_REMOVE = '  - '

MARKS = MARK_ADD, MARK_IDENTICAL, MARK_REMOVE
INDENTS = INDENT_ADD, INDENT_NOT_CHANGE, INDENT_REMOVE
MARK_ADD_AND_REMOVE = MARK_ADD, MARK_REMOVE


def stylish(diff: dict) -> str:
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


def set_indents_by_node(mark: str, count_indent: int, is_child: bool) -> tuple:
    """
    Set current indent by mark and count indent.

    Args:
        mark: mark changes
        count_indent: count deep indents
        is_child: node having children

    Returns:
        tuple: count indent, current indent by mark
    """
    _, current_indent = list(filter(
        lambda indent: mark == indent[0],
        zip(MARKS, INDENTS),
    ))[0]
    if mark == MARK_IDENTICAL:
        if is_child:
            return count_indent, ''
        return count_indent, current_indent
    if is_child:
        return count_indent + 1, current_indent
    return count_indent, current_indent


def ast_walk(node: dict, deep_indent=0) -> list:
    """
    Walk to difference structure tree.

    Args:
        node: difference tree
        deep_indent: count deepness tree

    Returns:
        list:
    """
    output = []
    for node_key, node_data in sorted(node.items()):
        if isinstance(node_data, tuple):
            for item_mark in node_data:
                mark, changes_data = item_mark
                is_children = isinstance(changes_data, dict)
                count_indent, current_indent = set_indents_by_node(
                    mark,
                    deep_indent,
                    is_children,
                )
                if is_children:
                    if mark in MARK_ADD_AND_REMOVE:
                        quote_in = format_result(
                            count_indent - 1,
                            '{',
                            node_key,
                            current_indent,
                        )
                        quote_out = format_result(count_indent, '}')
                    else:
                        quote_in = format_result(
                            count_indent,
                            '{',
                            node_key,
                            current_indent,
                        )
                        quote_out = format_result(count_indent + 1, '}')
                    output.append(quote_in)
                    output.extend(ast_walk(changes_data, deep_indent + 1))
                    output.append(quote_out)
                else:
                    output.append(format_result(
                        count_indent,
                        changes_data,
                        node_key,
                        current_indent,
                    ))
        else:
            current_indent = deep_indent + 1
            if isinstance(node_data, dict):
                output.append(format_result(current_indent, '{', node_key))
                output.extend(ast_walk(node_data, current_indent))
                output.append(format_result(current_indent, '}'))
            else:
                output.append(format_result(
                    current_indent,
                    node_data,
                    node_key,
                ))
    return output


def format_result(count_indent: int, element, node='', indent_spec='') -> str:
    """
    Format result.

    Args:
        count_indent: number of indents
        element: value by node
        node: name node key
        indent_spec: special indent show how data changes

    Returns:
        str:
    """
    if node:
        return '{indent}{indent_spec}{node}: {element}'.format(
            indent=INDENT * count_indent,
            indent_spec=indent_spec,
            node=node,
            element=element,
        )
    return '{indent}{element}'.format(
        indent=INDENT * count_indent,
        element=element,
    )
