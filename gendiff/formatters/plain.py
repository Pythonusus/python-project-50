from gendiff.utilities.edit_result_string import edit_result_string


def stringify(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f'\'{value}\''
    return str(value)


def format_data(diff):
    if not diff:
        return ''

    def inner(diff, property_path=[]):
        result = []
        for key in diff.keys():
            status = diff[key].get('status')
            value = diff[key].get('value')
            current_path = [*property_path, key]
            str_path = '.'.join(current_path)
            str_value = stringify(value)
            match status:
                case 'added':
                    result.append(f'Property \'{str_path}\' '
                                  f'was added with value: {str_value}')
                case 'deleted':
                    result.append(f'Property \'{str_path}\' was removed')
                case 'modified':
                    new_value = diff[key].get('new_value')
                    str_new_value = stringify(new_value)
                    result.append(f'Property \'{str_path}\' was updated. '
                                  f'From {str_value} to {str_new_value}')
                case 'nested':
                    result.append(inner(value, current_path))
        result = '\n'.join(result)
        return result

    return edit_result_string(inner(diff))
