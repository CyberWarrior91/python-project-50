"""Testing different formats"""
import pytest
from gendiff.format_maker import generate_diff


stylish_flat_fixture = open('tests/fixtures/stylish_fixture_flat.txt')
stylish_nested_fixture = open('tests/fixtures/stylish_nested_fixture.txt')
plain_flat_fixture = open('tests/fixtures/plain_fixture_flat.txt')
plain_nested_fixture = open('tests/fixtures/plain_fixture.txt')
json_flat_fixture = open('tests/fixtures/json_fixture.txt')
json_nested_fixture = open('tests/fixtures/json_nested_fixture.txt')


file1_flat = 'tests/fixtures/file1.json'
file2_flat = 'tests/fixtures/file2.json'
file1_nested = 'tests/fixtures/file1_nested.json'
file2_nested = 'tests/fixtures/file2_nested.json'
flat_stylish_result = generate_diff(file1_flat, file2_flat, 'stylish')
flat_plain_result = generate_diff(file1_flat, file2_flat, 'plain')
flat_json_result = generate_diff(file1_flat, file2_flat, 'json')
nested_stylish_result = generate_diff(file1_nested, file2_nested, 'stylish')
nested_plain_result = generate_diff(file1_nested, file2_nested, 'plain')
nested_json_result = generate_diff(file1_nested, file2_nested, 'json')


@pytest.mark.parametrize("result,expected", 
                         [(flat_stylish_result, stylish_flat_fixture),
                          (nested_stylish_result, stylish_nested_fixture),
                          (flat_plain_result, plain_flat_fixture),
                          (nested_plain_result, plain_nested_fixture),
                          (flat_json_result, json_flat_fixture),
                          (nested_json_result, json_nested_fixture),
                          ])
def test_formatters(result, expected):
    assert result == expected.read()
