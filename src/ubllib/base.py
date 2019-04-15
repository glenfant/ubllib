"""
===========
ubllib.base
===========

Base classes for documents and components
"""
import pathlib
import typing

from lxml import etree, objectify

from .validation import get_schema

FilePath = typing.NewType('FilePath', typing.Union[str, pathlib.Path])


class BaseDocument:
    """An ABC for all types of UBL documents

    Attributes:
        document: The ElementTree of the document
        root: The document root element
        root_tag (class): The expected root tag of the document
        minimal_xml (class): A minimalist valid UBL XML for the
    """
    root_tag = "{fake-namespace}override-this"
    minimal_xml = b"<important>Override this in subclasses</important>"

    def __init__(self, document: etree._ElementTree):
        self.document = document
        self.root = document.getroot()
        self.cleanup()

    @classmethod
    def from_filename(cls, filename: FilePath) -> 'BaseDocument':
        """Factory method

        Args:
            filename: relative or absolute path of an UBL document file

        Returns:
            A BaseDocument subclass instance (Invoice, ...)
        """
        with open(filename, 'rb') as stream:
            document = cls.from_file(stream)
        return document

    @classmethod
    def _make_parser(cls):
        """Makes a parser from the appropriate schema
        """
        schema = get_schema(cls.root_tag)
        parser = objectify.makeparser(schema=schema)
        return parser

    @classmethod
    def from_file(cls, stream: typing.BinaryIO) -> 'BaseDocument':
        """Factory method

        Args:
            stream: A binary file (like) open for reading

        Returns:
            A BaseDocument subclass instance (Invoice, ...)
        """
        parser = cls._make_parser()
        document = objectify.parse(stream, parser=parser)
        return cls(document)

    @classmethod
    def from_text(cls, text: typing.AnyStr) -> 'BaseDocument':
        """Factory method

        Args:
            text: An XML bytes string

        Returns:
            A BaseDocument subclass instance (Invoice, ...)
        """
        parser = cls._make_parser()
        document = objectify.fromstring(text, parser=parser)
        return cls(document)

    @classmethod
    def from_scratch(cls):
        """Factory method that builds a minimalist customizable document

        Returns:
            A BaseDocument subclass instance (Invoice, ...)
        """
        document = cls.from_text(cls.minimal_xml)
        return document

    def cleanup(self):
        # https://stackoverflow.com/questions/30232031/how-can-i-strip-namespaces-out-of-an-lxml-tree/30233635#30233635
        for element in self.root.xpath('descendant-or-self::*'):
            element.tag = etree.QName(element).localname
