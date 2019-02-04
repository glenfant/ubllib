#!/usr/bin/env python
"""
=================
Running all tests
=================

To have a fine grained control over the tests to run::

  python -m unittest -h
"""
import argparse
import sys
import unittest
from tests import all_tests


exit_code = 1

ap = argparse.ArgumentParser(epilog='Try: "python -m unittest -h" for more options.')
ap.add_argument('-v', '--verbosity', action='store', type=int, default=0, metavar="LEVEL",
                help="verbosity level: 0 (default), 1 or 2")
args = ap.parse_args()

results = unittest.TextTestRunner(verbosity=args.verbosity).run(all_tests())

issues_count = len(results.failures) + len(results.errors)
if issues_count == 0:
    exit_code = 0
sys.exit(exit_code)
