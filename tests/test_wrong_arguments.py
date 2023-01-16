import pytest
from gendiff.modules.gendiff_module import open_file


def test_failed():
    with pytest.raises(Exception):
     open_file('tests/fixtures/file1.json', 'tests/fixtures/file2.json')