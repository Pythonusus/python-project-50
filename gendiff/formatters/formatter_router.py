from gendiff.formatters import stylish

FORMATTERS = {
    'stylish': stylish.format_data
}


def select_formatter(formatter):
    return FORMATTERS[formatter]
