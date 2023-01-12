build:
		poetry build
package-install:
		pip install --user dist/*.whl --force-reinstall
check:
		python3 -m pytest
install:
		poetry install
test-coverage:
		coverage report -m
lint:
		poetry run flake8 gendiff

