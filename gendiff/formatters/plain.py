def plain_format(diff_result, path=''):
    result = []

    for node in diff_result:
        key = node['key']
        property_path = f"{path}{key}"

        if node['status'] == 'nested':
            result.append(plain_format(node['children'], f"{property_path}."))
        elif node['status'] == 'added':
            value = format_value(node['value'])
            result.append(f"Property '{property_path}' was added with value: "
                          f"{value}")
        elif node['status'] == 'removed':
            result.append(f"Property '{property_path}' was removed")
        elif node['status'] == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            result.append(f"Property '{property_path}' was updated. "
                          f"From {old_value} to {new_value}")

    return '\n'.join(result)


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
