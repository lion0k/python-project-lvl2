"""Json format."""

import json


def format_json(diff: list) -> str:
    """
    View style.

    Args:
        diff: difference structure

    Returns:
        str:
    """
    return json.dumps(diff, indent=4)
