import argparse


def run_argparse(argv=None):
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', help='set format of output:\
          json, plain or stylish given by default'
    )
    args = parser.parse_args(argv)
    return args.first_file, args.second_file, args.format
