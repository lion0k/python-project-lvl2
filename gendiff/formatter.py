"""Formatter interface."""

from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def format_diff(diff: list, output_format: str) -> str:
    """
    Format difference structure.

    Args:
        diff: difference structure
        output_format: format name

    Returns:
        str:
    """
    if output_format == 'stylish':
        return format_stylish(diff)
    if output_format == 'plain':
        return format_plain(diff)
    if output_format == 'json':
        return format_json(diff)
