"""
=================
ubllib.namespaces
=================

XML namespaces and associated utilities
"""
import functools
from lxml import etree

INVOICE_NS = "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"

prefix_namespaces = (
    # Main
    ("inv", INVOICE_NS),
    # Common
    ("cac", "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"),
    ("cbc", "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"),
    ("ext", "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"),
    # W3C
    ("xsd", "http://www.w3.org/2001/XMLSchema"),
    ("xsi", "http://www.w3.org/2001/XMLSchema-instance"),
)

prefix_ns_map = dict(prefix_namespaces)


def clark_tag(prefixed_tag: str) -> str:
    """Makes a clark notation tag from a prefixed tag name
    """
    splitted = prefixed_tag.split(":")
    if len(splitted) == 1:
        prefix = None
        tag = prefixed_tag
    else:
        prefix, tag = splitted
    return "{" + prefix_ns_map[prefix] + "}" + tag

# An XPath object that understands usual UBL prefixes
UBLXpath = functools.partial(etree.XPath, namespaces=prefix_ns_map)
