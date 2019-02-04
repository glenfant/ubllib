"""Misc fixtures and helpers for all tests"""

# FIXME: Provide anything that suits your package tests
# (custom TestCase classes, common fixtures, ...)
import functools
import os

tests_directory = os.path.dirname(os.path.abspath(__file__))
tests_abs_path = functools.partial(os.path.join, tests_directory)
