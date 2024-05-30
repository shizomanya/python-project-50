install:
	poetry install

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

check:
	flake8 .
	pytest --cov=.

package-install:
	poetry build
	python3 -m pip install --user dist/*.whl

selfcheck:
	poetry check

.PHONY: install test lint selfcheck check build
