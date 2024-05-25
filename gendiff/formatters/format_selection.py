from gendiff.formatters.json import json_format
from gendiff.formatters.plain import plain_format
from gendiff.formatters.stylish import stylish_format


def select_format(diff_result, format_name):
    if format_name == 'plain':
        return plain_format(diff_result)
    elif format_name == 'stylish':
        return stylish_format(diff_result)
    elif format_name == 'json':
        return json_format(diff_result)
    else:
        raise ValueError(f"Unsupported format: {format_name}")
