"""Difference structure."""

IDENTICAL = 'identical'
ADD = 'added'
REMOVE = 'removed'
UPDATE = 'updated'
NESTED = 'nested'


def build_difference(old_data, new_data) -> list:
    """
    Build difference structure.

    Args:
        old_data: first file
        new_data: second file

    Returns:
        list:
    """
    diff_result = []
    for key in sorted(old_data.keys() | new_data.keys()):
        changes = {'key': key}
        value_old_data = old_data.get(key)
        value_new_data = new_data.get(key)

        if value_old_data == value_new_data:
            changes['state'] = IDENTICAL
            changes['value'] = value_old_data
        elif key not in old_data:
            changes['state'] = ADD
            changes['value'] = value_new_data
        elif key not in new_data:
            changes['state'] = REMOVE
            changes['value'] = value_old_data
        elif isinstance(value_old_data, dict) and isinstance(value_new_data, dict):
            changes['state'] = NESTED
            changes['children'] = build_difference(value_old_data, value_new_data)
        else:
            changes['state'] = UPDATE
            changes['old_value'] = value_old_data
            changes['new_value'] = value_new_data

        diff_result.append(changes)
    return diff_result
