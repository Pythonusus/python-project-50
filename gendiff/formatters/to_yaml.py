import yaml


def format_data(diff):
    if not diff:
        return ''
    return yaml.safe_dump(diff)
