"""
======
ubllib
======

UBL (Universal Busines Language) version 2.1 objects parsing and marshalling.
"""

# FIXME: Please read http://pythonhosted.org/setuptools/setuptools.html to
#        customize in depth your setup script

from setuptools import setup
import pathlib
import sys

version = '1.0.0'

this_directory = pathlib.Path(__file__).absolute().parent

long_description = '\n\n'.join(
    [path.read_text().strip()
     for path in (this_directory / 'README.rst',
                  this_directory / 'doc' / 'source' / 'contributors.rst',
                  this_directory / 'doc' / 'source' / 'changes.rst')]
)

dev_require = ['Sphinx', 'pytest']

setup(name='ubllib',
      version=version,
      description="UBL (Universal Busines Language) version 2.1 objects parsing and marshalling.",
      long_description=long_description,
      # FIXME: Add more classifiers from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "License :: OSI Approved :: MIT license"
      ],
      keywords='UBL Business',  # FIXME: Add whatefer fits
      author='Gilles Lenfant',
      author_email='gilles.lenfant@gmail.com',
      url='http://pypi.python.org/pypi/ubllib',
      license='MIT license',
      packages='ubllib',
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # 3rd party
          'setuptools'
          # Others
      ],
      entry_points={},
      tests_require=dev_require,
      test_suite='tests.all_tests',
      extras_require={
          'dev': dev_require
      })
