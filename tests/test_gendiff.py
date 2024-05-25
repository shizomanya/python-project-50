import pytest
from pathlib import Path
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize(
    "file1, file2, right_answer, format_name",
    [
        ('file1_tree.json', 'file2_tree.json', 'correct_result.txt', 'json'),
        ('file1_tree.yml', 'file2_tree.yml', 'correct_result.txt', 'json'),
        ('file1_tree.json', 'file2_tree.json', 'plain_result.txt', 'plain'),
        ('file1_tree.yml', 'file2_tree.yml', 'plain_result.txt', 'plain'),
        ('file1_tree.json', 'file2_tree.json', 'stylish_result.txt', 'stylish'),
        ('file1_tree.yml', 'file2_tree.yml', 'stylish_result.txt', 'stylish'),
    ]
)
def test_generate_diff(file1, file2, right_answer, format_name):
    path_dict1 = get_fixture_path(file1)
    path_dict2 = get_fixture_path(file2)
    path_result = get_fixture_path(right_answer)

    with open(path_result) as f:
        expected_result = f.read().strip()

    result = generate_diff(path_dict1, path_dict2, format_name)

    assert result.strip() == expected_result.strip()


def get_fixture_path(file_name):
    return Path(Path(__file__).parent.absolute() / 'fixtures' / file_name)
