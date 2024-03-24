import pytest
from gendiff.gendiff import generate_diff

FLAT1_JSON = 'gendiff/tests/fixtures/flat1.json'
FLAT2_JSON = 'gendiff/tests/fixtures/flat2.json'
FLAT1_YAML = 'gendiff/tests/fixtures/flat1.yaml'
FLAT2_YAML = 'gendiff/tests/fixtures/flat2.yml'
EXPECTED_FLAT = 'gendiff/tests/fixtures/expected_flat.txt'


@pytest.mark.parametrize('file_path1, file_path2, expected_file_path', [
    (FLAT1_JSON, FLAT2_JSON, EXPECTED_FLAT),
    (FLAT1_YAML, FLAT2_YAML, EXPECTED_FLAT),
])
def test_gendiff(file_path1, file_path2, expected_file_path):
    with open(expected_file_path) as expected:
        assert generate_diff(file_path1, file_path2) == expected.read()
