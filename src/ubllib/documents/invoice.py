"""
========================
ubllib.documents.invoice
========================
"""
from lxml import etree

from ..base import BaseDocument
from ..namespaces import INVOICE_NS, clark_tag


class Invoice(BaseDocument):
    namespace = INVOICE_NS
    root_tag = clark_tag('inv:Invoice')

