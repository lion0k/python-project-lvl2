"""Difference structure."""

MARK_IDENTICAL = 'identical'
MARK_ADD = 'added'
MARK_REMOVE = 'removed'
MARK_UPDATE = 'updated'


def get_data_by_key(node_key, node):
    """
    Get data by node key.

    Args:
        node_key: possible key in node
        node: node

    Returns:
        any: value by node
        or
        empty tuple for marking if key not found in node
    """
    if node_key in node:
        return node.get(node_key)
    return ()


def set_marker_by_key(node_key, old_data, new_data):
    """
    Set data change marking.

    Args:
        node_key: key node
        old_data: data before
        new_data: new data

    Returns:
        dict:
    """
    def set_state_and_value(state: str, node_value):
        """
        Set state and value.

        Args:
            state: mark state changes
            node_value: data by node
        """
        changes['state'] = state
        changes['value'] = node_value

    changes = {'key': node_key}
    value_old_data = get_data_by_key(node_key, old_data)
    value_new_data = get_data_by_key(node_key, new_data)

    if value_old_data == value_new_data:
        set_state_and_value(MARK_IDENTICAL, value_old_data)
    elif isinstance(value_old_data, tuple):
        set_state_and_value(MARK_ADD, value_new_data)
    elif isinstance(value_new_data, tuple):
        set_state_and_value(MARK_REMOVE, value_old_data)
    elif isinstance(value_old_data, dict) and isinstance(value_new_data, dict):
        changes['children'] = build_difference(value_old_data, value_new_data)
    else:
        changes['state'] = MARK_UPDATE
        changes['value'] = {
            'remove_value': value_old_data,
            'add_value': value_new_data,
        }
    return changes


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
    union_keys = sorted(old_data.keys() | new_data.keys())
    for key in union_keys:
        diff_result.append(set_marker_by_key(key, old_data, new_data))
    return diff_result


def get_state_node(node: dict) -> str:
    """
    Get state node.

    Args:
        node: node

    Returns:
        str:
    """
    return node['state']


def get_key(node: dict) -> str:
    """
    Get key by node.

    Args:
        node: node

    Returns:
        str:
    """
    return node['key']


def get_value(node: dict):
    """
    Get value by key.

    Args:
        node: node

    Returns:
        any:
    """
    return node['value']


def is_children_exist(node: dict) -> bool:
    """
    Check exist having children in node.

    Args:
        node: node

    Returns:
        bool:
    """
    return 'children' in node
