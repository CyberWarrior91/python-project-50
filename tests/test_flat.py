"""Flat data testing"""

from gendiff.modules.gendiff_module import generate_diff

def test_flat_json():
    fixture = open('tests/fixtures/flat_fixture.txt')
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert result == fixture.read()
    
def test_flat_yml():
    fixture = open('tests/fixtures/flat_fixture.txt')
    result = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')
    assert result == fixture.read()