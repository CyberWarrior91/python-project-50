install:
		poetry install
package-install:
		pip install --user dist/*.whl --force-reinstall
lint:
		poetry run flake8 gendiff
test:
		poetry run pytest
test-coverage:
		poetry run pytest --cov=gendiff --cov-report xml tests
selfcheck:
		poetry check

check:		selfcheck test lint

build:
		poetry build

