# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Frumentarii',
    version='1.0.0',
    description='The client side application for local network chat',
    long_description=readme,
    author='Jack Easton',
    author_email='jack.east0n@outlook.co.uk',
    url='https://github.com/perseusnova',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

