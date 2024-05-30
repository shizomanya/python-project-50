import json
import yaml


def parse_file(file_path):
    file_path_str = str(file_path)
    file_extension = file_path_str.split('.')[-1]
    if file_extension in ['json']:
        return get_dict_from_file(file_path_str, 'json')
    elif file_extension in ['yml', 'yaml']:
        return get_dict_from_file(file_path_str, 'yaml')
    else:
        raise ValueError(f"Unsupported format: .{file_extension}")


def get_dict_from_file(file_path, file_extension):
    if file_extension == 'json':
        with open(file_path) as f:
            return json.load(f)
    elif file_extension in ['yml', 'yaml']:
        with open(file_path) as f:
            return yaml.safe_load(f)
    else:
        raise ValueError(f"Unsupported format: {file_extension}")
