from gendiff.modules.argparse_module import run_argparse


def test_run_argparse(capsys):
    run_argparse(['first_file', 'tests/fixtures/file1.json', 'second_file', 'tests/fixtures/file2.json'])
    fixture = open('tests/fixtures/flat_fixture.txt')
    captured = capsys.readouterr()
    assert captured.out == fixture