from gendiff.parser import parse_file
from gendiff.make_diff import make_diff
from gendiff.formatters.format_selection import select_format


def generate_diff(file_path1, file_path2, format_name='stylish'):
    dict1 = parse_file(file_path1)
    dict2 = parse_file(file_path2)
    diff_result = make_diff(dict1, dict2)

    return select_format(diff_result, format_name)
