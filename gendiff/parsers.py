"""Data parser."""

import json

import yaml

YAML_EXTENSION = 'yml', 'yaml'


def parse_data(stream, format_parse: str) -> dict:
    """
    Parse data.

    Args:
        stream: data
        format_parse: type of parser

    Returns:
        dict:
    """
    if format_parse == 'json':
        return json.loads(stream)
    if format_parse in YAML_EXTENSION:
        return yaml.safe_load(stream)
