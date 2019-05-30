#!/usr/bin/env python2
# -*- coding: utf-8 -*-

""" My application """

from __future__ import absolute_import, print_function

import logging
import sys
from builtins import input, range

# root logger config
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def main():
    logging.info("Hello world")


if __name__ == "__main__":
    main()
