# puck (Python Update cheCKer)

A tool to get an overview on which Python dependencies need updates.

It takes one or more requirements text files or setup py files and prints
updated versions of them, if there are any. Requirements are only parsed if
they are *pinned*, i.e. of the form ```abc==1.2.3```.

## Installation

* `pip install puck`

## Usage

Check one or more requirements text files:

```puck -f requirements.txt```

Check setup.py files:

```puck -s setup.py```

Check a combination of files:

```puck -s setup.py -f requirements-test.txt -f requirements-prod.txt```
