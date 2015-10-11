#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name='kaxo',
    description='File Manager',
    version='0.0.1',
    install_requires=['docopt', 'urwid'],
    packages=['kaxo'],
    entry_points={"console_scripts": ["kaxo = kaxo.kaxo:main"]}
)
