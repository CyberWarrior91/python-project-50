from gendiff.modules.argparse_module import run_argparse


def test_run_argparse():
    file_paths = run_argparse(['tests/fixtures/file1.json', 'tests/fixtures/file2.json'])
    assert file_paths == ('tests/fixtures/file1.json', 'tests/fixtures/file2.json')