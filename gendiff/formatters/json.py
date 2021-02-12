"""Json format."""

import json


def json_formatter(diff: dict) -> str:
    """
    View style.

    Args:
        diff: difference structure

    Returns:
        str:
    """
    return json.dumps(diff, sort_keys=True, indent=4)
