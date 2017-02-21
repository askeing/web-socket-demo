#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from setuptools import setup, find_packages

CURRENT_PATH = os.path.dirname(__file__)

DEFAULT_REQUIREMENT_DOC = os.path.join(CURRENT_PATH, 'requirements.txt')


# dependencies
with open(DEFAULT_REQUIREMENT_DOC) as f:
    deps = f.read().splitlines()


version = '0.0.1'


# main setup script
setup(
    name='web-socket-demo',
    version=version,
    description='Demo the Web Socket Server and Client',
    author='Askeing',
    author_email='askeing@gmail.com',
    license='MPL',
    install_requires=deps,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
