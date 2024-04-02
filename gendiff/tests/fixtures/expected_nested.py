NESTED_DIFF = {
    'common': {
        'follow': {'value': False, 'status': 'added'},
        'setting1': {'value': 'Value 1', 'status': 'unchanged'},
        'setting2': {'value': 200, 'status': 'deleted'},
        'setting3': {'value': True, 'status': 'deleted'},
        'setting4': {'value': 'blah blah', 'status': 'added'},
        'setting5': {'value': {'key5': 'value5'}, 'status': 'added'},
        'setting6': {
            'doge': {
                'wow': {'value1': '', 'value2': 'so much', 'status': 'modified'}
            },
            'key': {'value': 'value', 'status': 'unchanged'},
            'ops': {'value': 'vops', 'status': 'added'}
        }
    },
    'group1': {
        'baz': {'value1': 'bas', 'value2': 'bars', 'status': 'modified'},
        'foo': {'value': 'bar', 'status': 'unchanged'},
        'nest': {
            'value1': {'key': 'value'},
            'value2': 'str',
            'status': 'modified'
        }
    },
    'group2': {
        'value': {'abc': 12345, 'deep': {'id': 45}}, 'status': 'deleted'
    },
    'group3': {
        'value': {'deep': {'id': {'number': 45}}, 'fee': 100500},
        'status': 'added'
    }
}
