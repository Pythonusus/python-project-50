import json

import yaml
from gendiff.utilities.is_empty_file import is_empty_file


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


def select_loader(file_path):
    if is_empty_file(file_path):
        return load_empty_file
    if file_path.endswith('json'):
        return load_json
    if file_path.endswith('yaml') or file_path.endswith('yml'):
        return load_yaml
