"""Choose formatter."""

from gendiff.formatters.json import json_formatter
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def formatter(output_format: str):
    """
    Get formatter function.

    Args:
        output_format: data output format name

    Returns:
        function:
    """
    if output_format == 'stylish':
        return stylish
    elif output_format == 'plain':
        return plain
    elif output_format == 'json':
        return json_formatter
