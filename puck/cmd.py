#!/usr/bin/env python

import click
from puck import __version__ as version
from puck.backend import high_version_backend, pypi_backend
from puck.output import output_fn
from puck.parser import parse_requirements_file, parse_setup_py

NAME = 'puck'

""" puck is a CLI utility which parses requirements.txt and setup.py files for
pinned dependencies and displays updated version information."""


@click.command()
@click.option(
    '--requirements-file',
    '-f',
    multiple=True,
    type=click.Path(exists=True),
    help='parse a requirements.txt file',
)
@click.option(
    '--setup-py-file',
    '-s',
    multiple=True,
    type=click.Path(exists=True),
    help='parse a setup.py file',
)
@click.option(
    '--show-all',
    '-a',
    is_flag=True,
    help='show up-to-date entries as well'
)
@click.option(
    '--test-backend',
    '-t',
    is_flag=True,
    help='query a dummy backend instead of PyPI'
)
@click.option(
    '--output',
    '-o',
    default='default',
    type=click.Choice(['default', 'json']),
    help='output format'
)
@click.version_option(
    version=version,
    prog_name=NAME
)
def check(
    requirements_file=None,
    setup_py_file=None,
    show_all=False,
    test_backend=False,
    backend=pypi_backend,
    output='default'
):
    """Checks Python projects for outdated dependencies"""
    results = []

    if test_backend:
        backend = high_version_backend

    if requirements_file:
        for rf in requirements_file:
            results.extend(parse_requirements_file(rf, backend=backend))

    if setup_py_file:
        for sf in setup_py_file:
            results.extend(parse_setup_py(sf, backend=backend))

    output_fn.get(output)(
        [
            entry for entry in results
            if (entry['pinned_version'] != entry['latest_version'] or show_all)
        ]
    )


if __name__ == '__main__':
    check()
