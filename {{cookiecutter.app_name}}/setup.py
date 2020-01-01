#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# Setup requirements
try:
    from setuptools import setup, find_packages
    from setuptools.command.install import install
except ImportError:
    print(
        "setuptools is needed in order to build. Install it using your package manager (usually python-setuptools) or via pip (pip install setuptools)."
    )
    sys.exit(1)


def read_file(file_name):
    """Read file and return its contents."""
    with open(file_name, "r") as f:
        return f.read()


# Load library version
sys.path.insert(0, os.path.abspath("lib"))

from {{cookiecutter.app_name}}.release import __author__, __email__, __version__  # isort:skip


def get_dynamic_setup_params():
    """Add dynamically calculated setup params to static ones."""

    return {
        # Retrieve the long description from the README
        "long_description": read_file("README.md")
    }


# Inspired from https://circleci.com/blog/continuously-deploying-python-packages-to-pypi-with-circleci/
class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""

    description = "Verify that the git tag matches the version"

    def run(self):
        tag = os.getenv("DRONE_TAG", "unknown")

        if tag != __version__:
            info = "Git tag: {} does not match the version of this app: {}".format(
                tag, __version__
            )
            sys.exit(info)


# Extra requirements installable using pip -e '.[<extra>]'
EXTRAS_REQUIRE = {
    "docs": ["sphinx", "sphinxcontrib.mermaid>=0.3.1", "sphinx-rtd-theme>=0.4.3"],
    "tests": [
        "black",
        "tox",
        "isort",
        "coverage-badge>=1.0.1",
        "coverage>=4.5.4",
        "flake8>=3.7.9",
        "pytest-cov>=2.8.1",
        "pytest-logger>=0.5.1",
        "pytest-runner>=5.2",
        "pytest>=5.2.2",
    ],
}

# Development requirements
EXTRAS_REQUIRE["dev"] = (
    EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["docs"] + ["pre-commit"]
)

static_setup_params = dict(
    name="{{cookiecutter.app_name}}",
    version=__version__,
    description=("{{cookiecutter.app_description}}"),
    keywords="python",
    author=__author__,
    author_email=__email__,
    url="",
    package_dir={"": "lib"},
    packages=find_packages("lib"),
    package_data={},
    zip_safe=False,
    scripts=[],
    license="GNU GPLv3",
    install_requires=[],
    extras_require=EXTRAS_REQUIRE,
    test_suite="test",
    cmdclass={"verify": VerifyVersionCommand},
)


if __name__ == "__main__":
    setup_params = dict(static_setup_params, **get_dynamic_setup_params())
    setup(**setup_params)
