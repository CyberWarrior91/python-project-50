"""Nested data testing"""

from gendiff.modules.gendiff_module import generate_diff

def test_nested_json():
    fixture = open('tests/fixtures/nested_fixture.txt')
    result = generate_diff('tests/fixtures/file1_nested.json', 'tests/fixtures/file2_nested.json')
    assert result == fixture.read()
    
def test_nested_yml():
    fixture = open('tests/fixtures/flat_fixture.txt')
    result = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')
    assert result == fixture.read()