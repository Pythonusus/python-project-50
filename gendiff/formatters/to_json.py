import json


def format_data(diff):
    if not diff:
        return ''
    return json.dumps(diff, indent=2)
