DOCKER_IMAGE := ydmt/dreem-ppai
VERSION := $(shell git describe --always --dirty --long)
	
default:
	python3 -m venv venv
	cd venv/bin && . activate && cd ../..
	pip install -r requirements.txt
	pip install .

upgrade-dependencies:
	rm -f requirements.txt
	pip freeze > requirements.txt

push_to_pypi:
	rm -fr dist
	python3 -m build
	twine upload -r pypi dist/*

