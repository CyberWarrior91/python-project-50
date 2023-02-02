from gendiff import generate_diff
from gendiff.modules.argparse_module import run_argparse


def main():
    first_file, second_file, format_name = run_argparse()
    diff = generate_diff(first_file, second_file, format_name)
    print(diff)


if __name__ == '__main__':
    main()
