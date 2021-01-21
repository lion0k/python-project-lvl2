gendiff:
		poetry run gendiff

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
