#!/usr/bin/env python
from setuptools import find_packages, setup

from puck import __version__ as version

desc = '''

puck (Python Update cheCKer)
============================

A tool to get an overview on which Python dependencies need updates.

*Code and documentation:* `<https://github.com/NativeInstruments/puck>`_.
'''


test_deps = [
    "pytest==3.4.0",
    "pytest-cov==2.5.1",
    "pytest-random==0.02",
    "mock==2.0.0"
]

extras = {
    'test': test_deps
}


setup(
    name='puck',
    version=version,
    description='Python Update cheCKer',
    long_description=desc,
    author='Native Instruments GmbH',
    author_email='cloud-devops+github@native-instruments.de',
    license='MIT',
    url='https://github.com/NativeInstruments/puck',
    packages=find_packages(
        exclude=['test*.py']
    ),
    # production requirements
    install_requires=[
        "click==6.7",
        "six==1.11.0",
    ],
    tests_require=test_deps,
    extras_require=extras,
    include_package_data=True,
    entry_points={
        'console_scripts': ['puck = puck.cmd:check']
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'
    ],
)
