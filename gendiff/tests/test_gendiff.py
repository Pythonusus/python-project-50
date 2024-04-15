import pytest
from gendiff.gendiff import generate_diff

FLAT1_JSON = 'gendiff/tests/fixtures/flat1.json'
FLAT2_JSON = 'gendiff/tests/fixtures/flat2.json'
FLAT1_YAML = 'gendiff/tests/fixtures/flat1.yaml'
FLAT2_YAML = 'gendiff/tests/fixtures/flat2.yml'
NESTED1_JSON = 'gendiff/tests/fixtures/nested1.json'
NESTED2_JSON = 'gendiff/tests/fixtures/nested2.json'
NESTED1_YAML = 'gendiff/tests/fixtures/nested1.yml'
NESTED2_YAML = 'gendiff/tests/fixtures/nested2.yaml'
EXPECTED_FLAT_STYLISH = 'gendiff/tests/fixtures/expected_flat_stylish.txt'
EXPECTED_NESTED_STYLISH = 'gendiff/tests/fixtures/expected_nested_stylish.txt'
EXPECTED_FLAT_PLAIN = 'gendiff/tests/fixtures/expected_flat_plain.txt'
EXPECTED_NESTED_PLAIN = 'gendiff/tests/fixtures/expected_nested_plain.txt'
EXPECTED_FLAT_JSON = 'gendiff/tests/fixtures/expected_flat.json'
EXPECTED_NESTED_JSON = 'gendiff/tests/fixtures/expected_nested.json'
EXPECTED_FLAT_YAML = 'gendiff/tests/fixtures/expected_flat.yaml'
EXPECTED_NESTED_YAML = 'gendiff/tests/fixtures/expected_nested.yaml'


@pytest.mark.parametrize('file_path1, file_path2, expected_file_path', [
    (FLAT1_JSON, FLAT2_JSON, EXPECTED_FLAT_STYLISH),
    (FLAT1_YAML, FLAT2_YAML, EXPECTED_FLAT_STYLISH),
    (NESTED1_JSON, NESTED2_JSON, EXPECTED_NESTED_STYLISH),
    (NESTED1_YAML, NESTED2_YAML, EXPECTED_NESTED_STYLISH),
])
def test_gendiff_stylish(file_path1, file_path2, expected_file_path):
    with open(expected_file_path) as expected:
        assert generate_diff(file_path1, file_path2) == expected.read()


@pytest.mark.parametrize('file_path1, file_path2, expected_file_path', [
    (FLAT1_JSON, FLAT2_JSON, EXPECTED_FLAT_PLAIN),
    (FLAT1_YAML, FLAT2_YAML, EXPECTED_FLAT_PLAIN),
    (NESTED1_JSON, NESTED2_JSON, EXPECTED_NESTED_PLAIN),
    (NESTED1_YAML, NESTED2_YAML, EXPECTED_NESTED_PLAIN),
])
def test_gendiff_plain(file_path1, file_path2, expected_file_path):
    with open(expected_file_path) as expected:
        assert generate_diff(
            file_path1, file_path2, formatter='plain'
        ) == expected.read()


@pytest.mark.parametrize('file_path1, file_path2, expected_file_path', [
    (FLAT1_JSON, FLAT2_JSON, EXPECTED_FLAT_JSON),
    (FLAT1_YAML, FLAT2_YAML, EXPECTED_FLAT_JSON),
    (NESTED1_JSON, NESTED2_JSON, EXPECTED_NESTED_JSON),
    (NESTED1_YAML, NESTED2_YAML, EXPECTED_NESTED_JSON),
])
def test_gendiff_json(file_path1, file_path2, expected_file_path):
    with open(expected_file_path) as expected:
        assert generate_diff(
            file_path1, file_path2, formatter='json'
        ) == expected.read()


@pytest.mark.parametrize('file_path1, file_path2, expected_file_path', [
    (FLAT1_JSON, FLAT2_JSON, EXPECTED_FLAT_YAML),
    (FLAT1_YAML, FLAT2_YAML, EXPECTED_FLAT_YAML),
    (NESTED1_JSON, NESTED2_JSON, EXPECTED_NESTED_YAML),
    (NESTED1_YAML, NESTED2_YAML, EXPECTED_NESTED_YAML),
])
def test_gendiff_yaml(file_path1, file_path2, expected_file_path):
    with open(expected_file_path) as expected:
        assert generate_diff(
            file_path1, file_path2, formatter='yaml'
        ) == expected.read()
