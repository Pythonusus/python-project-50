from gendiff.formatters.formatter_router import select_formatter
from gendiff.utilities.data_comparator import compare_data
from gendiff.utilities.loaders import load_file_data


def generate_diff(file_path1, file_path2, formatter='stylish'):
    data1 = load_file_data(file_path1)
    data2 = load_file_data(file_path2)
    diff = compare_data(data1, data2)
    format_data = select_formatter(formatter)
    return format_data(diff)
