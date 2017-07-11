# puck (Python Update cheCKer)

[![Travis](https://img.shields.io/travis/NativeInstruments/puck.svg?style=flat-square)](https://travis-ci.org/NativeInstruments/puck) [![license](https://img.shields.io/github/license/NativeInstruments/puck.svg?style=flat-square)](https://github.com/NativeInstruments/puck/blob/master/LICENSE) [![PyPI](https://img.shields.io/pypi/v/puck.svg)](https://pypi.python.org/pypi/puck)


A tool to get an overview on which Python dependencies need updates.

It takes one or more requirements text files or setup py files and prints
updated versions of them, if there are any. Requirements are only parsed if
they are *pinned*, i.e. of the form ```abc==1.2.3```.

## Installation

```
$ git clone https://github.com/NativeInstruments/puck.git
$ cd puck
$ pip install .
```

*installation from PyPI coming soon* 

## Usage

Check one or more requirements text files:

```puck -f requirements.txt```

Check setup.py files:

```puck -s setup.py```

Check a combination of files:

```puck -s setup.py -f requirements-test.txt -f requirements-prod.txt```
