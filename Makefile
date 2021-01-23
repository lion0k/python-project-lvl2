gendiff:
		poetry run gendiff file1.json file2.json

build:
		poetry build

install:
		poetry install

lint:
		poetry run flake8 gendiff

publish:
		poetry publish --dry-run

package-install:
		pip install --user dist/*.whl

.PHONY: gendiff