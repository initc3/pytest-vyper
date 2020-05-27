#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


install_requires = [
    "eth-tester[py-evm]>=0.3.0b1,<0.4",
    "lark-parser>=0.7.8,<1",
    "pytest",
    "vyper",
    "web3",
]

dev_requires = ["ipdb", "ipython"]
docs_requires = ["Sphinx"]
tests_requires = [
    "black",
    "coverage",
    "flake8",
    "flake8-import-order",
    "pep8-naming",
    "pytest-cov",
]
extras_require = {
    "dev": dev_requires + docs_requires + tests_requires,
    "docs": docs_requires,
    "tests": tests_requires,
}

setup(
    name="pytest-vyper",
    version="0.1.0",
    author="Syvain Bellemare",
    author_email="sbellem@gmail.com",
    maintainer="Syvain Bellemare",
    maintainer_email="sbellem@gmail.com",
    license="Apache Software License 2.0",
    url="https://github.com/sbellem/pytest-vyper",
    description="Plugin for the vyper smart contract language.",
    long_description=read("README.rst"),
    py_modules=["pytest_vyper"],
    python_requires=">=3.6",
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
    ],
    entry_points={"pytest11": ["vyper = pytest_vyper"]},
    extras_require=extras_require,
)
