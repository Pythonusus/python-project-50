#!/usr/bin/env python3
"""
"""
from gendiff.generate_diff import generate_diff
from gendiff.utilities.cli import parse_args


def main():
    args = parse_args()
    file1, file2, format_ = args.first_file, args.second_file, args.format
    print(generate_diff(file1, file2, format_))


if __name__ == '__main__':
    main()
