# -*- coding: utf-8 -*-
import os
from distutils.core import setup
from setuptools import find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='pydkan',
    version='0.1',
    author=u'NuCivic',
    author_email='devops@nucivic.com',
    license='BSD licence, see LICENCE.txt',
    description='Python Client for dkan dataset api',
    packages=['dkan'],
    include_package_data=True,
    zip_safe=False,
    entry_points = {},
    install_requires=required,
)