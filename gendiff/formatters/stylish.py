from gendiff.formatters.edit_result_string import edit_result_string

SPACES_COUNT = 4
OFFSET = 2
REPLACER = ' '


def stringify(data, depth):
    if not isinstance(data, dict):
        return str(data)

    current_indent = REPLACER * SPACES_COUNT * depth
    deep_indent = REPLACER * SPACES_COUNT * (depth + 1)
    result = ['{']
    for key, value in data.items():
        result.append(f'{deep_indent}{key}: {stringify(value, depth + 1)}')
    result.append(f'{current_indent}' + '}')
    result = '\n'.join(result)
    return result


def format_data(diff):
    if not diff:
        return ''

    def inner(diff, depth):
        current_indent = REPLACER * SPACES_COUNT * depth
        deep_indent = REPLACER * SPACES_COUNT * (depth + 1)
        deep_indent_with_offset = deep_indent[:-OFFSET]
        result = ['{']
        for key in diff.keys():
            value = diff[key].get('value')
            str_value = stringify(value, depth + 1)
            status = diff[key].get('status')
            match status:
                case 'added':
                    result.append(
                        f'{deep_indent_with_offset}+ {key}: {str_value}'
                    )
                case 'deleted':
                    result.append(
                        f'{deep_indent_with_offset}- {key}: {str_value}'
                    )
                case 'unchanged':
                    result.append(f'{deep_indent}{key}: {str_value}')
                case 'modified':
                    new_value = diff[key].get('new_value')
                    str_new_value = stringify(new_value, depth + 1)
                    result.append(
                        f'{deep_indent_with_offset}- {key}: {str_value}'
                    )
                    result.append(
                        f'{deep_indent_with_offset}+ {key}: {str_new_value}'
                    )
                case 'nested':
                    result.append(
                        f'{deep_indent}{key}: {inner(value, depth + 1)}'
                    )
        result.append(f'{current_indent}' + '}')
        result = '\n'.join(result)
        return result

    return edit_result_string(inner(diff, 0))
