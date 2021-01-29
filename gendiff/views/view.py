"""View format styles."""

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
