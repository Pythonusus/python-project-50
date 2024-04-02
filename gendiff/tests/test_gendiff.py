import pytest
from gendiff.formatters import stylish
from gendiff.gendiff import compare_data, generate_diff
from gendiff.loaders import select_loader
from gendiff.tests.fixtures.expected_flat import FLAT_DIFF
from gendiff.tests.fixtures.expected_nested import NESTED_DIFF

FLAT1_JSON = 'gendiff/tests/fixtures/flat1.json'
FLAT2_JSON = 'gendiff/tests/fixtures/flat2.json'
FLAT1_YAML = 'gendiff/tests/fixtures/flat1.yaml'
FLAT2_YAML = 'gendiff/tests/fixtures/flat2.yml'
NESTED1_JSON = 'gendiff/tests/fixtures/nested1.json'
NESTED2_JSON = 'gendiff/tests/fixtures/nested2.json'
NESTED1_YAML = 'gendiff/tests/fixtures/nested1.yml'
NESTED2_YAML = 'gendiff/tests/fixtures/nested2.yaml'
EXPECTED_FLAT = 'gendiff/tests/fixtures/expected_flat.txt'
EXPECTED_NESTED = 'gendiff/tests/fixtures/expected_nested.txt'


@pytest.mark.parametrize('file_path1, file_path2, expected', [
    (FLAT1_JSON, FLAT2_JSON, FLAT_DIFF),
    (FLAT1_YAML, FLAT2_YAML, FLAT_DIFF),
    (NESTED1_JSON, NESTED2_JSON, NESTED_DIFF),
    (NESTED1_YAML, NESTED2_YAML, NESTED_DIFF)])
def test_compare_data(file_path1, file_path2, expected):
    file1_loader = select_loader(file_path1)
    file2_loader = select_loader(file_path2)
    data1 = file1_loader(file_path1)
    data2 = file2_loader(file_path2)
    print(f'TEST PRINT: {data1}')
    print(f'TEST PRINT: {data2}')
    diff = compare_data(data1, data2)
    assert diff == expected


@pytest.mark.parametrize('data, expected_file_path', [
    (FLAT_DIFF, EXPECTED_FLAT),
    (NESTED_DIFF, EXPECTED_NESTED)])
def test_stylish(data, expected_file_path):
    with open(expected_file_path) as expected:
        assert stylish.format_data(data) == expected.read()


@pytest.mark.parametrize('file_path1, file_path2, expected_file_path', [
    (FLAT1_JSON, FLAT2_JSON, EXPECTED_FLAT),
    (FLAT1_YAML, FLAT2_YAML, EXPECTED_FLAT),
    (NESTED1_JSON, NESTED2_JSON, EXPECTED_NESTED),
    (NESTED1_YAML, NESTED2_YAML, EXPECTED_NESTED)])
def test_gendiff(file_path1, file_path2, expected_file_path):
    with open(expected_file_path) as expected:
        assert generate_diff(file_path1, file_path2) == expected.read()
