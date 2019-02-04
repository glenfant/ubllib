# -*- coding: utf-8 -*-
"""\
======
ubllib
======

Tests package
"""
import unittest

from .resources import tests_directory

def all_tests():
    return unittest.defaultTestLoader.discover(tests_directory)
