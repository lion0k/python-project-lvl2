"""View format styles."""

from gendiff.views.json import json
from gendiff.views.plain import plain
from gendiff.views.stylish import stylish


def view(view_format: str):
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
        return json
