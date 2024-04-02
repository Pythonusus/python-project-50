#!/usr/bin/env python3
"""
"""
from gendiff.cli import args
from gendiff.gendiff import generate_diff


def main():
    file1_path, file2_path = args.first_file, args.second_file
    formatter = args.format
    print(generate_diff(file1_path, file2_path, formatter))


if __name__ == '__main__':
    main()
