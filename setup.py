#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://github.com/kennethreitz/setup.py ❤️ ✨ 🍰 ✨

import os
from setuptools import setup, find_packages

NAME = 'jl'
DESCRIPTION = 'Library for parsing JSON lines.'
KEYWORDS = 'json jl'
URL = 'https://github.com/croqaz/JL'
AUTHOR = 'Cristi Constantin'
EMAIL = 'cristi.constantin@speedpost.net'

here = os.path.abspath(os.path.dirname(__file__))
about = {}

try:
    with open(os.path.join(here, 'README.md')) as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec(f.read(), about)

setup(
    version=about['__version__'],
    name=NAME,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=KEYWORDS,
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    license='MIT',
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    zip_safe=True,
    python_requires='>= 3.6',
    extras_require={
        'dev': ['flake8', 'codecov'],
        'test': ['pytest', 'pytest-cov'],
    },
    classifiers=[
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
    ])
