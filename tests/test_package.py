# -*- coding: utf-8 -*-
"""Unit tests of ubllib"""

import sys
import unittest

import resources


###
# Test layers
###

def setUpModule():
    # Setups for all tests of this module
    return

def tearDownModule():
    # Cleanups for all tests of this module
    return

###
# Test cases
###

class SomeTest(unittest.TestCase):
    """FIXME: describe here what you are testing
    """
    @classmethod
    def setUpClass(cls):
        # Setups before first test of this class
        return

    @classmethod
    def tearDownClass(cls):
        # Cleanups after last test of this class
        return

    def setUp(self):
        # Setups before each test of this class
        return

    def tearDown(self):
        # Cleanups after each test of this class
        return

    def test_fake(self):
        """FIXME: provide your first test here
        """
        self.assertEqual(1, 1)
        return
