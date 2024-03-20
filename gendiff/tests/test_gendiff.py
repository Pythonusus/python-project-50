from gendiff.gendiff import generate_diff


def test_gendiff():
    assert generate_diff(
        'gendiff/tests/fixtures/test_file1.json',
        'gendiff/tests/fixtures/test_file2.json'
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