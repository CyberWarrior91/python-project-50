"""Plain data testing"""

from gendiff.modules.gendiff_module import generate_diff

def test_plain_flat():
    fixture = open('tests/fixtures/plain_fixture_flat.txt')
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'plain')
    assert result == fixture.read()


def test_plain_nested():
    fixture = open('tests/fixtures/plain_fixture.txt')
    result = generate_diff('tests/fixtures/file1_nested.json', 'tests/fixtures/file2_nested.json', 'plain')
    assert result == fixture.read()

