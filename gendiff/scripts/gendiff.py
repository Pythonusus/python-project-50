#!/usr/bin/env python3
"""
"""
from gendiff.generate_diff import generate_diff
from gendiff.utilities.cli import parse_args


def main():
    args = parse_args()
    file1_path, file2_path = args.first_file, args.second_file
    formatter = args.format
    print(generate_diff(file1_path, file2_path, formatter))


if __name__ == '__main__':
    main()
