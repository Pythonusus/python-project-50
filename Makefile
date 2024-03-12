install:
	poetry install

gendiff:
	poetry run gendiff

help:
	poetry run gendiff -h

lint:
	poetry run flake8 gendiff
	poetry run pylint gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

.PHONY: install gendiff help lint build publish package-install package-reinstall