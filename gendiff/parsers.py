"""Data parser."""

import json

import yaml

YAML_EXTENSION = 'yml', 'yaml'


def parse_data(stream, parser: str) -> dict:
    """
    Parse data.

    Args:
        stream: data
        parser: type of parser

    Returns:
        dict:
    """
    if parser == 'json':
        return json.loads(stream)
    if parser in YAML_EXTENSION:
        return yaml.safe_load(stream)
