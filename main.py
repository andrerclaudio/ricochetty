#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Application Entry Point.
"""

import logging

logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s [%(levelname)s]: %(message)s"
)

LOG = logging.getLogger(__name__)


def application() -> None:
    LOG.info("Starting application...")


if __name__ == "__main__":
    application()
