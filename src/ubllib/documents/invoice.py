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
    tag = 'Invoice'

    def __init__(self):
        """
        """

    @classmethod
    def from_element(cls, tree: etree._ElementTree):
        """Factory"""
        root = tree.getroot()
        assert root.tag == f'{{{cls.namespace}}}{cls.tag}'
