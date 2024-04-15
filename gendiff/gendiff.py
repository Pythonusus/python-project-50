from gendiff.formatters.formatter_router import select_formatter
from gendiff.utilities.data_comparator import compare_data
from gendiff.utilities.loaders import select_loader


def generate_diff(file_path1, file_path2, formatter='stylish'):
    file1_loader = select_loader(file_path1)
    file2_loader = select_loader(file_path2)
    data1 = file1_loader(file_path1)
    data2 = file2_loader(file_path2)
    diff = compare_data(data1, data2)
    format_data = select_formatter(formatter)
    return format_data(diff)
