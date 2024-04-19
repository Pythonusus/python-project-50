import json
import os

import yaml


def is_empty_file(file_path):
    stats = os.stat(file_path)
    return True if stats.st_size == 0 else False


def load_json(file_path):
    with open(file_path) as f:
        data = json.load(f)  # dict
    return data


def load_yaml(file_path):
    with open(file_path) as f:
        data = yaml.safe_load(f)
    return data


def load_empty_file(_):
    """Imitates data load from empty file.

    Args:
        _ (str): _ argument is passed to make load_empty_file function usage
                 similar to other loaders in this module. However, no file is
                 opened.

    Returns:
        dict: always returns empty dict instance
    """
    return {}


def get_file_extension(file_path):
    parts = file_path.split('.')
    if len(parts) == 1 or parts[-1] == '':
        return ''
    return parts[-1]


def select_loader(file_path):
    if is_empty_file(file_path):
        return load_empty_file
    if file_path.endswith('json'):
        return load_json
    if file_path.endswith('yaml') or file_path.endswith('yml'):
        return load_yaml

    file_extension = get_file_extension(file_path)
    raise ValueError(f'Unsupported file extension: {file_extension}')


def load_file_data(file_path):
    loader = select_loader(file_path)
    return loader(file_path)
