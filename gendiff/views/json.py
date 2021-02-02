"""Json format."""

from gendiff.engine import converting


def json(diff: dict) -> str:
    """
    View style.

    Args:
        diff: difference structure

    Returns:
        str:
    """
    return converting(diff, sort_keys=True, indent=4)
