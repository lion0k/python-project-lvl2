"""Choose formatter."""

from gendiff.formatters.json import json_formatter
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def format_diff(diff: list, output_format: str) -> str:
    """
    Format difference structure.

    Args:
        diff: difference structure
        output_format: format name

    Returns:
        str:
    """
    formatter = get_formatter(output_format)
    return formatter(diff)


def get_formatter(formatter: str):
    """
    Get format function.

    Args:
        formatter: format name

    Returns:
        function:
    """
    if formatter == 'stylish':
        return stylish
    elif formatter == 'plain':
        return plain
    elif formatter == 'json':
        return json_formatter
