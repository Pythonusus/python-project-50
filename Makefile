install:
	poetry install

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 brain_games
	poetry run pylint brain_games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

.PHONY: install gendiff lint build publish package-install package-reinstall