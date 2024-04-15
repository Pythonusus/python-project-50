from pathlib import Path


def is_empty_file(path_to_file):
    return True if Path(path_to_file).stat().st_size == 0 else False
