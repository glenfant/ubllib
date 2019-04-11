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
    """Makes a clark notation tag from a prefixed tag.

    Args:
        prefixed_tag: tag preceded by a prefix and ":" like "inv:Invoice"

    Returns:
        The tag in CLark notation as expected by lxml

    Example:
        >>> clark_tag("inv:foo")
        '{urn:oasis:names:specification:ubl:schema:xsd:Invoice-2}foo'
        >>> clark_tag("foo")
        'foo'
    """
    parts = prefixed_tag.split(":")
    count = len(parts)
    if count == 1:
        out = prefixed_tag
    elif count == 2:
        prefix, tag = parts
        out = "{" + prefix_ns_map[prefix] + "}" + tag
    else:
        raise ValueError(f'Tag "{prefixed_tag}" is not a valid prefixed tag (2 or more ":")')
    return out


# An XPath object that understands usual UBL prefixes
UBLXpath = functools.partial(etree.XPath, namespaces=prefix_ns_map)
