from gendiff.formatters import plain, stylish

FORMATTERS = {
    'stylish': stylish.format_data,
    'plain': plain.format_data
}


def select_formatter(formatter):
    return FORMATTERS[formatter]
