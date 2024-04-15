import json

import yaml


def load_json(file_path):
    with open(file_path) as f:
        data = json.load(f)  # dict
    return data


def load_yaml(file_path):
    with open(file_path) as f:
        data = yaml.safe_load(f)
    return data


def select_loader(file_path):
    if file_path.endswith('json'):
        return load_json
    if file_path.endswith('yaml') or file_path.endswith('yml'):
        return load_yaml
