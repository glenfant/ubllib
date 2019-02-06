"""
==========================
Fixtures de tests globales
==========================
"""
import pathlib

import pytest


@pytest.fixture
def test_directory() -> pathlib.Path:
    """The absolute path of this tests package directory"""
    this_directory = pathlib.Path(__file__).absolute().parent
    return this_directory
