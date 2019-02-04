# -*- coding: utf-8 -*-
"""Doctests of ubllib"""

import doctest
import glob

from resources import tests_abs_path

# Add resources available in the file doctests
filedoctest_globs = {
    'dummy': lambda: None
}

def filedoctest_setup(test):
    # Add fixtures for your doctest files
    # See https://docs.python.org/3/library/doctest.html#doctest.DocFileSuite
    return

def filedoctest_teardown(test):
    # Cleanup fixtures for your doctest files
    # See https://docs.python.org/3/library/doctest.html#doctest.DocFileSuite
    return

def load_tests(loader, tests, ignore):
    # See https://docs.python.org/3/library/doctest.html#unittest-api

    # Run the tests in the .rst files of this directory
    doctest_files = glob.glob(tests_abs_path('test_*.rst'))
    tests.addTests(doctest.DocFileSuite(*doctest_files, module_relative=False,
                                        setUp=filedoctest_setup, tearDown=filedoctest_teardown,
                                        globs=filedoctest_globs))

    # Run the doctests in the various modules
    import ubllib
    modules_with_doctests = (ubllib,)
    for module in modules_with_doctests:
        tests.addTests(doctest.DocTestSuite(module))
    return tests
