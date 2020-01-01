#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logging.config import dictConfig
from {{cookiecutter.app_name}}.logging_config import DEFAULT_LOGGING_CONFIG

# Initialize logging
dictConfig(DEFAULT_LOGGING_CONFIG)
