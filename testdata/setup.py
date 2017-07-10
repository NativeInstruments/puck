#!/usr/bin/env python
from setuptools import find_packages, setup

desc = '''

puck (Python Update cheCKer)
============================

A tool to get an overview on which Python dependencies need updates.

*Code and documentation:* `<https://github.com/NativeInstruments/puck>`_.
'''

setup(
    name='puck',
    version='1.0.0',
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
        "six==1.10.0",
    ],
    tests_require=[
        "flake8==3.3.0",
        "isort==4.2.5",
        "pytest==3.0.7",
        "pytest-cov==2.4.0",
        "pytest-random==0.02",
        "tox==2.6.0",
        "click==6.7",
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': ['puck=puck.puck:main']
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
)
