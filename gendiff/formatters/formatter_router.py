from gendiff.formatters import plain, stylish, to_json, to_yaml

FORMATTERS = {
    'stylish': stylish.format_data,
    'plain': plain.format_data,
    'json': to_json.format_data,
    'yaml': to_yaml.format_data,
}


def select_formatter(diff_format):
    formatter = FORMATTERS.get(diff_format)
    if formatter is None:
        raise ValueError(f'Unsupported format: {diff_format}')
    return formatter
