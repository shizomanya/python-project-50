def stylish_format(diff_result, depth=0):
    lines = []
    indent = '    ' * depth
    closing_indent = '    ' * depth if depth > 0 else ''

    status_templates = {
        'added': f"{indent}  + {{key}}: {{value}}",
        'removed': f"{indent}  - {{key}}: {{value}}",
        'unchanged': f"{indent}    {{key}}: {{value}}",
        'changed': [
            f"{indent}  - {{key}}: {{old_value}}",
            f"{indent}  + {{key}}: {{new_value}}"
        ],
        'nested': f"{indent}    {{key}}: {{value}}"
    }

    for node in diff_result:
        key = node['key']
        status = node['status']

        if status in status_templates:
            template = status_templates[status]
            if status == 'changed':
                lines.extend([
                    template[0].format(
                        key=key,
                        old_value=format_value(node['old_value'], depth + 1)
                    ),
                    template[1].format(
                        key=key,
                        new_value=format_value(node['new_value'], depth + 1)
                    )
                ])
            elif status == 'nested':
                nested_value = stylish_format(node['children'], depth + 1)
                lines.append(template.format(key=key, value=nested_value))
            else:
                lines.append(template.format(
                    key=key,
                    value=format_value(node['value'], depth + 1)
                ))
    result = '{'
    for line in lines:
        result += f'\n{line}'
    result += '\n' + closing_indent + '}'
    return result


def format_value(value, depth):
    indent = '    ' * depth
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            line = f"{indent}    {k}: {format_value(v, depth + 1)}"
            lines.append(line)
        result = '{'
        for line in lines:
            result += f'\n{line}'
        result += '\n' + indent + '}'
        return result

    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)
