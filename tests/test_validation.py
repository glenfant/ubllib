import pathlib
from lxml import etree
import pytest

from ubllib.validation import validate

this_directory = pathlib.Path(__file__).absolute().parent
all_invoice_files = [p for p in (this_directory / 'data' / 'invoices').iterdir()
                     if p.suffix == '.xml']


@pytest.mark.parametrize('invoice_path', all_invoice_files)
def test_validation(invoice_path):
    with open(invoice_path, 'rb') as invoice_stream:
        tree = etree.parse(invoice_stream)

    # We ensure these are invoices
    assert tree.getroot().tag.endswith('Invoice')

    # We validate
    assert validate(tree)
