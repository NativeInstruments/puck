# puck (Python Update cheCKer)

[![Travis](https://img.shields.io/travis/NativeInstruments/puck.svg?style=flat-square)](https://travis-ci.org/NativeInstruments/puck) [![license](https://img.shields.io/github/license/NativeInstruments/puck.svg?style=flat-square)](https://github.com/NativeInstruments/puck/blob/master/LICENSE) [![PyPI](https://img.shields.io/pypi/v/puck.svg)](https://pypi.python.org/pypi/puck)


A tool to get an overview on which Python dependencies need updates.

It takes one or more requirements text files or setup py files and prints
updated versions of them, if there are any. Requirements are only parsed if
they are *pinned*, i.e. of the form ```abc==1.2.3```.

## Installation

```
$ pip install puck
```

## Usage

```
 $ puck --help
Usage: puck [OPTIONS]

  Checks Python projects for outdated dependencies

Options:
  -f, --requirements-file PATH  parse a requirements.txt file
  -s, --setup-py-file PATH      parse a setup.py file
  -a, --show-all                show up-to-date entries as well
  -t, --test-backend            query a dummy backend instead of PyPI
  -o, --output [default|json]   output format
  --version                     Show the version and exit.
  --help                        Show this message and exit.
```


## Examples

Check one or more requirements text files:

```puck -f requirements.txt```

Check setup.py files:

```puck -s setup.py```

Check a combination of files:

```puck -s setup.py -f requirements-test.txt -f requirements-prod.txt```

Use the json output function:

```$ puck -f testdata/requirements.txt -o json
[{"source": "src/puck/testdata/requirements.txt", "name": "pytest-cov", "latest_version": "2.5.1", "pinned_version": "2.4.0"}]
```


## Changelog

### 1.0.4 (2017-07-11)

* First public release
