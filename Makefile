build:
		poetry build
package-install:
		pip install --user dist/*.whl --force-reinstall
make lint:
		poetry run flake8 gendiff
make install:
		pip install poetry

