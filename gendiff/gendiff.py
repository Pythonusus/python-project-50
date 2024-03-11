import json


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))  # dict
    data2 = json.load(open(file_path2))  # dict
    diffs = ['{']

    keys = set().union(data1.keys(), data2.keys())
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if value1 is None:  # d.get(keys) returns None if key not in d
            diffs.append(f' + {key}: {data2[key]}')
        elif value2 is None:
            diffs.append(f' - {key}: {data1[key]}')
        elif value1 == value2:
            diffs.append(f' {key}: {data1[key]}')
        else:
            diffs.append(f' - {key}: {data1[key]}')
            diffs.append(f' + {key}: {data2[key]}')
    diffs.append('}')
    return '\n'.join(diffs)
