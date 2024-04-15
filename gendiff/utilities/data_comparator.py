def compare_data(data1, data2):
    diff = dict()

    keys = sorted(set().union(data1.keys(), data2.keys()))
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            nested_diff = compare_data(value1, value2)
            diff[key] = {
                'value': nested_diff,
                'status': 'nested'
            }
        elif key not in data1.keys():
            diff[key] = {
                'value': value2,
                'status': 'added'
            }
        elif key not in data2.keys():
            diff[key] = {
                'value': value1,
                'status': 'deleted'
            }
        elif value1 == value2:
            diff[key] = {
                'value': value1,
                'status': 'unchanged'
            }
        else:
            diff[key] = {
                'value': value1,
                'new_value': value2,
                'status': 'modified'
            }
    return diff
