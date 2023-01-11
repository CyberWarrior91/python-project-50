"""Float data testing"""

from gendiff.modules.gendiff_module import generate_diff

def test_flat():
    fixture = open('tests/fixtures/flat_fixture.txt')
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert result == fixture.read()