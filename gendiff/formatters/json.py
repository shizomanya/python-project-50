import json


def json_value(value):
    if isinstance(value, dict):
        return {k: json_value(v) for k, v in value.items()}
    elif value is None:
        return None
    elif isinstance(value, bool):
        return str(value).lower()
    return value


def json_format(diff_result):
    json_result = json_value(diff_result)
    return json.dumps(json_result, indent=4)
