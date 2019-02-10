======
ubllib
======

UBL (Universal Business Language) version 2.1 objects parsing and marshalling.

UBL is an industry standard XML interchange format for business documents (invoices, manifests, ...) specified by the
ISO/IEC 19845:2015 standard.

Read more about this standard and download associated resources from https://www.iso.org/standard/66370.html

Provided features
=================

- Create Python business objects from UBL documents, with optional validation.
- Serialize Python business objects to UBL documents.
- Supported subset of UBL 2.1 documents are:

    - Invoice

.. warning::

   ``ubllib`` is **not** an ERP and does not suport UBL processes. It is just intended to help reading, writing and
   validating the structure of UBL business objects.

Developer notes
===============

Please use a virtualenv to maintain this package, but I should not need to say that.

Grab the source from the SCM repository:

.. code:: console

  $ pip install .[dev]

Run the tests:

.. code:: console

  $ pytest

Build the Sphinx documentation:

.. code:: console

  $ python setup.py build_sphinx
  $ firefox build/sphinx/html/index.html

License
=======

This software is protected by the terms of MIT license.

Links
=====

Project home page

  http://www.mystuff.com/project

Source code

  http://www.mystuff.com/source

Issue tracker

  http://www.mystuff.com/issues
