build:
		poetry build
package-install:
		pip install --user dist/*.whl --force-reinstall
check:
		poetry run flake8 gendiff
		poetry run pytest
install:
		poetry install
test-coverage:
		poetry run pytest --cov=gendiff --cov-report xml

