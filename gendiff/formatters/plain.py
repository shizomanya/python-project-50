def plain_format(diff_result, path=''):
    result = []

    for node in diff_result:
        result.append(format_node(node, path))

    return '\n'.join(filter(None, result))


def format_node(node, path):
    key = node['key']
    property_path = f"{path}{key}"

    if node['status'] == 'nested':
        return plain_format(node['children'], f"{property_path}.")
    elif node['status'] == 'added':
        value = format_value(node['value'])
        return f"Property '{property_path}' was added with value: {value}"
    elif node['status'] == 'removed':
        return f"Property '{property_path}' was removed"
    elif node['status'] == 'changed':
        old_value = format_value(node['old_value'])
        new_value = format_value(node['new_value'])
        return (
            f"Property '{property_path}' was updated. "
            f"From {old_value} to {new_value}"
        )
    elif node['status'] == 'unchanged':
        return None
    else:
        raise ValueError(f"Unsupported node status: {node['status']}")


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    return value
