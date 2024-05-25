#!/usr/bin/env python3
from gendiff.generate_diff import generate_diff
from gendiff.tools.cli import parser_args


def main():
    file1_path, file2_path, format_name = parser_args()
    print(generate_diff(file1_path, file2_path, format_name))


if __name__ == '__main__':
    main()
