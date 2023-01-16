from gendiff.modules.argparse_module import run_argparse



def test_run_argparse_json():
    file_paths = run_argparse(['somefile1.json', 'file2.json'])
    assert file_paths == ('somefile1.json', 'file2.json')


def test_run_argparse_yml():
    file_paths = run_argparse(['tests/fixtures/file1.yml', 'tests/fixtures/file2.yml'])
    assert file_paths == ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')