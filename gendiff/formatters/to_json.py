import json


def format_data(diff):
    return json.dumps(diff, indent=2)
