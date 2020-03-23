#!/usr/bin/env python

from distutils.core import setup
import setuptools

setup(name='PRICE',
      version='0.0.1',
      description='Fiserv PRICE API Client',
      author='Fiserv',
      author_email='',
      packages=setuptools.find_packages(exclude=["docs", "tests"]),
      python_requires=">=3.6",
      requires=['PrettyTable', 'requests'],
      )
