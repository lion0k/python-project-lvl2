"""View format styles."""

from gendiff.formatters.json import json_view
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def output(view_format: str):
    """
    Output views function.

    Args:
        view_format: format for view

    Returns:
        function:
    """
    if view_format == 'stylish':
        return stylish
    elif view_format == 'plain':
        return plain
    elif view_format == 'json':
        return json_view
