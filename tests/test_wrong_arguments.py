import pytest
from gendiff.format_maker import open_file


def test_failed():
    with pytest.raises(Exception):
        open_file('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
