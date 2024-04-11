from gendiff.formatters import plain, stylish, to_json

FORMATTERS = {
    'stylish': stylish.format_data,
    'plain': plain.format_data,
    'json': to_json.format_data
}


def select_formatter(formatter):
    return FORMATTERS[formatter]
