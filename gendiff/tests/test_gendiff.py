from gendiff.gendiff import generate_diff


def test_gendiff_json():
    assert generate_diff(
        'gendiff/tests/fixtures/flat1.json',
        'gendiff/tests/fixtures/flat2.json'
    ) == (
        '{\n'
        ' - follow: false\n'
        ' host: hexlet.io\n'
        ' - proxy: 123.234.53.22\n'
        ' - timeout: 50\n'
        ' + timeout: 20\n'
        ' + verbose: true\n'
        '}'
    )


def test_gendiff_yaml():
    assert generate_diff(
        'gendiff/tests/fixtures/flat1.yaml',
        'gendiff/tests/fixtures/flat2.yml'
    ) == (
        '{\n'
        ' - follow: false\n'
        ' host: hexlet.io\n'
        ' - proxy: 123.234.53.22\n'
        ' - timeout: 50\n'
        ' + timeout: 20\n'
        ' + verbose: true\n'
        '}'
    )
