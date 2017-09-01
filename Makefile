.DEFAULT_GOAL=all

all: setup test

setup:
	pip install tox
	python setup.py develop

test:
	tox

clean:
	rm -rf puck.egg-info
	find . -name "*.pyc" -type f -delete
	rm -rf puck/__pycache__
	rm -rf .eggs
	rm -rf .tox
	rm -rf build
	rm -rf dist
	rm -rf htmlcov
	rm -f junit-out.xml
	rm -f .coverage
	rm -rf .cache

wheel:
	python3 setup.py bdist_wheel --universal

install:
	python setup.py install
