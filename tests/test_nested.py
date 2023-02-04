"""Nested data testing"""

from gendiff import generate_diff


def test_nested_json():
    fixture = open('tests/fixtures/nested_fixture.txt')
    result = generate_diff(
        'tests/fixtures/file1_nested.json',
        'tests/fixtures/file2_nested.json',
        'stylish'
        )
    assert result == fixture.read()


def test_nested_yml():
    fixture = open('tests/fixtures/nested_fixture.txt')
    result = generate_diff('tests/fixtures/file1_nested.yml',
                            'tests/fixtures/file2_nested.yml',
                            'stylish')
    assert result == fixture.read()
