import argparse

from gendiff.formatters.formatter_router import FORMATTERS


def parse_args():
    parser = argparse.ArgumentParser(
        description=('Compares two configuration files '
                     'and shows a difference.')
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        choices=FORMATTERS.keys(),
        help=('set format of output (default: stylish)'),
        default='stylish'
    )
    args = parser.parse_args()
    return args
