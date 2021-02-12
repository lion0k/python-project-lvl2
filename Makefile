install:
	poetry install

test:
	poetry run pytest tests

test-coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml

lint:
	poetry run flake8 gendiff tests

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: gendiff