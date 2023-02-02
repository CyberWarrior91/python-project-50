"""Json data testing"""

from gendiff.modules.gendiff_module import generate_diff

def test_flat_json():
    fixture = open('tests/fixtures/json_fixture.txt')
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'json')
    assert result == fixture.read()


def test_nested_json():
    fixture = open('tests/fixtures/json_nested_fixture.txt')
    result = generate_diff('tests/fixtures/file1_nested.json', 'tests/fixtures/file2_nested.json', 'json')
    assert result == fixture.read()