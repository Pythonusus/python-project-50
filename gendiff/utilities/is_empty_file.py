import os


def is_empty_file(path_to_file):
    stats = os.stat(path_to_file)
    return True if stats.st_size == 0 else False
