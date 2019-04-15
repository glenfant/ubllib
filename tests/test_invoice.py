from ubllib.documents import Invoice
from . import this_directory


def test_invoice_3518():
    test_file = this_directory / "data" / "invoices" / "EDFSAI03518.xml"
    invoice = Invoice.from_filename(test_file)
    dummy = 0
