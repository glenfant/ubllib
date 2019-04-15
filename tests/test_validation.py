from io import BytesIO

import pytest
from lxml import etree

from ubllib.validation import validate
from . import this_directory

all_invoice_files = tuple((this_directory / "data" / "invoices").glob("*.xml"))


@pytest.mark.parametrize("invoice_path", all_invoice_files)
def test_invoice_validation(invoice_path):
    with open(invoice_path, "rb") as invoice_stream:
        tree = etree.parse(invoice_stream)

    # We ensure these are invoices
    assert tree.getroot().tag.endswith("Invoice")

    # We validate
    assert validate(tree)
    assert validate(tree, raise_=True)


def test_invoice_invalidation():
    fake_invoice_xml = b"""
    <Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2">
    </Invoice>
    """
    tree = etree.parse(BytesIO(fake_invoice_xml))
    assert not validate(tree)


def test_validate_not_ubl():
    not_ubl_xml = b"""<a>anything</a>"""
    tree = etree.parse(BytesIO(not_ubl_xml))
    assert not validate(tree)
