install:
	poetry install

run brain-games:
	poetry run brain-games

run brain-even:
	poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games

.PHONY: install 
