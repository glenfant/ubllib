"""
======
ubllib
======

UBL (Universal Busines Language) version 2.1 objects parsing and marshalling.
"""

import logging
import pkg_resources

# Custom logger
LOG = logging.getLogger(name=__name__)
LOG.addHandler(logging.NullHandler())

# PEP 396 style version marker
try:
    __version__ = pkg_resources.get_distribution('ubllib').version
except:
    LOG.warning("Could not get the package version from pkg_resources")
    __version__ = 'unknown'
