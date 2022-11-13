DOCKER_IMAGE := ydmt/dreem-ppai
VERSION := $(shell git describe --always --dirty --long)
default:
	pip3 uninstall dreem-ppai -y
	pip3 install .
	
init:
	pip install -r requirements.txt
	pip3 install .

pin-dependencies:
	pip install -U pip-tools
	pip-compile requirements.in

upgrade-dependencies:
	pip install -U pip pip-tools
	pip-compile -U requirements.in > requirements.txt

push_to_pypi:
	rm -fr dist
	python3 -m build
	twine upload -r pypi dist/*

