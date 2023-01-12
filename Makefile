build:
		poetry build
package-install:
		pip install --user dist/*.whl --force-reinstall
check:
		poetry run flake8 gendiff
		pytest
install:
		pip install poetry
test-coverage:
		coverage report -m

