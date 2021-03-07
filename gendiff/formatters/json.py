"""JSON format."""

import json


def format_json(diff: list) -> str:
    """
    Format to JSON.

    Args:
        diff: difference structure

    Returns:
        str:
    """
    return json.dumps(diff, indent=4)
