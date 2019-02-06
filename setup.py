"""
======
ubllib
======

UBL (Universal Busines Language) version 2.1 objects parsing and marshalling.
"""

# FIXME: Please read http://pythonhosted.org/setuptools/setuptools.html to
#        customize in depth your setup script

import pathlib
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

VERSION = '1.0.0'

this_directory = pathlib.Path(__file__).absolute().parent

long_description = '\n\n'.join(
    [path.read_text().strip()
     for path in (this_directory / 'README.rst',
                  this_directory / 'doc' / 'source' / 'contributors.rst',
                  this_directory / 'doc' / 'source' / 'changes.rst')]
)

dev_require = ['Sphinx', 'pytest']


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import shlex
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


setup(name='ubllib',
      version=VERSION,
      description="UBL (Universal Busines Language) version 2.1 objects parsing and marshalling.",
      long_description=long_description,
      # FIXME: Add more classifiers from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Topic :: Text Processing :: Markup :: XML",
          "Topic :: Office/Business",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3 :: Only",
          "Programming Language :: Python :: 3.6"
          "Programming Language :: Python :: 3.7",
          "License :: OSI Approved :: MIT License"
      ],
      keywords='UBL Business',
      author='Gilles Lenfant',
      author_email='gilles.lenfant@gmail.com',
      url='http://pypi.python.org/pypi/ubllib',
      license='MIT license',
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # 3rd party
          'setuptools',
          'lxml'
      ],
      entry_points={},
      tests_require=dev_require,
      test_suite='tests.all_tests',
      extras_require={
          'dev': dev_require
      },
      cmdclass={
          'test': PyTest
      }
      )
