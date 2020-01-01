#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

DEFAULT_LOGGING_CONFIG = dict(
    version=1,
    formatters={
        "default": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    handlers={
        "default": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": logging.DEBUG,
        },
        "dev": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": logging.DEBUG,
        },
    },
    root={"handlers": ["default"], "level": logging.DEBUG},
)
