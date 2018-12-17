#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Sentiant",
    description="Un jeu d'initiation a l'IA, programmez le comportement de fourmis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pyrofoux/SentiAnt",
    version="bite.couille.poile",
    license="oups",
    author="Andreas Bresser",
    packages=find_packages(),
    tests_require=["pathfinding"],
    include_package_data=True,
    install_requires=["pathfinding"],
)
