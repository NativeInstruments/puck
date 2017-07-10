import re

import pkg_resources
from puck.backend import pypi_backend


"""Logic related to parsing requirements text files and setup.py files for
pinned versions of the form `abc===1.2.3`"""


def parse_requirement(line, source, backend=pypi_backend):
    """
    Parses a given line as a valid requirements line in the form `abc==1.2.3`
    and returns a dict with information.

    @param line: str containing a valid requirements line
    @param source: str representing from which file this line was taken
    @param backend: backend function to use to fetch information
    """
    try:
        r = pkg_resources.Requirement.parse(line)
        if '==' in line:
            current_version = line.split('==', 1)[-1]
            latest = backend(r.name)
            return {
                'name': r.name,
                'pinned_version': current_version,
                'latest_version': latest,
                'source': source,
            }
    except ValueError as e:
        print("Fail {} {}".format(line, e))


def parse_requirements_file(requirements_file, backend=pypi_backend):
    """Parses a requirements.txt type file"""
    results = []
    with open(requirements_file, 'r') as rfile:
        for line in rfile.readlines():
            results.append(
                parse_requirement(
                    line.strip(),
                    requirements_file,
                    backend=backend,
                )
            )
    return results


def parse_setup_py(setup_py, backend=pypi_backend):
    """Parses a setup.py file"""
    results = []
    with open(setup_py, 'r') as sfile:
        for line in sfile.readlines():
            req = re.search('[\w\-\_]+==[\w\.]+', line.strip())
            if req:
                requirement = req.group()
                results.append(
                    parse_requirement(
                        requirement,
                        setup_py,
                        backend=backend,
                    )
                )
    return results
