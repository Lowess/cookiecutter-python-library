# :trident: {{cookiecutter.app_name | capitalize}}

[![Build Status](https://cloud.drone.io/api/badges/{{cookiecutter.github_username }}/{{cookiecutter.app_name}}/status.svg)](https://cloud.drone.io/{{cookiecutter.github_username }}/{{cookiecutter.app_name}})
[![Coverage Status](https://coveralls.io/repos/github/{{cookiecutter.github_username }}/{{cookiecutter.app_name}}/badge.svg?branch=master)](https://coveralls.io/github/{{cookiecutter.github_username }}//{{cookiecutter.app_name}}?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/psf/black)
[![Linter: flake8](https://img.shields.io/badge/linter-flake8-blue.svg)](http://flake8.pycqa.org/en/latest/)
[![Linter: tests](https://img.shields.io/badge/tests-tox-yellow.svg)](hhttps://tox.readthedocs.io/en/latest)
[![Documentation Status](https://readthedocs.org/projects//{{cookiecutter.app_name}}/badge/?version=latest)](https:///{{cookiecutter.app_name}}.readthedocs.io/en/latest/?badge=latest)

## Developer - Getting-Started

* Makefile

```bash
# Install development requirements
make dev

# Setup pre-commit hook locally
pre-commit install

# Run full tests
make tests

# Build Sphinx documentation locally
make docs
```

* IDE configuration

VSCode `settings.json`

```json
{
  "editor.formatOnSaveTimeout": 3000,
  "editor.codeActionsOnSaveTimeout": 3000,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.linting.enabled": true,
  "python.formatting.provider": "black",
  "python.formatting.blackPath": "~/.pyenv/shims/black",
  "python.sortImports.args": [
    "-rc",
    "--settings-path",
    "${workspaceFolder}",
  ],
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  },
  "python.pythonPath": "/Users/florian/.pyenv/versions/<VENV>/bin/python",
  "python.venvPath": "~/.pyenv/shims",
  "editor.formatOnPaste": false,
  "editor.formatOnSave": true,
}
```

* Formatting & Linters

 The project uses [Flake8](http://flake8.pycqa.org/en/latest/) linter and [Black](https://black.readthedocs.io/en/latest/) autoformatter

* Tests

Tests are automated with [Tox](https://tox.readthedocs.io/en/latest/) and run with [Pytest](https://docs.pytest.org/en/latest/) suite. [Codecoverage](https://coverage.readthedocs.io/en/latest/) is also reported during test runs.

* Documentation

The documentation can be genered with [Sphinx](https://www.sphinx-doc.org/en/2.0/)

Made with ♥ by {{cookiecutter.author_fullname}}
