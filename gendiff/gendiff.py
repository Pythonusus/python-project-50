from gendiff.formatters.formatter_router import select_formatter
from gendiff.loaders import select_loader


def compare_data(data1, data2):
    diffs = ['{']

    keys = sorted(set().union(data1.keys(), data2.keys()))
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if value1 is None:  # d.get(keys) returns None if key not in d
            diffs.append(f'  + {key}: {data2[key]}')
        elif value2 is None:
            diffs.append(f'  - {key}: {data1[key]}')
        elif value1 == value2:
            diffs.append(f'    {key}: {data1[key]}')
        else:
            diffs.append(f'  - {key}: {data1[key]}')
            diffs.append(f'  + {key}: {data2[key]}')
    diffs.append('}')
    result = '\n'.join(diffs)
    return edit_result_string(result)


def generate_diff(file_path1, file_path2, formatter='stylish'):
    file1_loader = select_loader(file_path1)
    file2_loader = select_loader(file_path2)
    data1 = file1_loader(file_path1)
    data2 = file2_loader(file_path2)
    diff = compare_data(data1, data2)
    format_data = select_formatter(formatter)
    return format_data(diff)
