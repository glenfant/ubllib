"""
==========================
Fixtures de tests globales
==========================
"""
import pathlib
from . import this_directory

import pytest


@pytest.fixture
def test_directory() -> pathlib.Path:
    """The absolute path of this tests package directory"""
    return this_directory
