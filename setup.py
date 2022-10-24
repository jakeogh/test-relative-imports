# -*- coding: utf-8 -*-

import sys

from setuptools import find_packages
from setuptools import setup

if not sys.version_info[0] == 3:
    sys.exit("Python 3 is required. Use: 'python3 setup.py install'")

dependencies = ["click"]

config = {
    "version": "0.1",
    "name": "test_relative_imports",
    "url": "https://github.com/jakeogh/test-relative-imports",
    "license": "ISC",
    "author": "Justin Keogh",
    "author_email": "github.com@v6y.net",
    "description": "testing relative imports",
    "long_description": __doc__,
    "packages": find_packages(exclude=["tests"]),
    "package_data": {"test_relative_imports": ["py.typed"]},
    "include_package_data": True,
    "zip_safe": False,
    "platforms": "any",
    "install_requires": dependencies,
    "entry_points": {
        "console_scripts": [
            "test-relative-imports=test_relative_imports.test_relative_imports:clitest",
        ],
    },
}

setup(**config)
