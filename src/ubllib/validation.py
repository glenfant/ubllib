"""
=================
ubllib.validation
=================

Validates xml data against schema
"""
import typing as t
import warnings
from functools import lru_cache

from lxml import etree

from . import package_directory
from .namespaces import clark_tag, UBLXpath

schema_2_1_main = package_directory / "schemas_2_1" / "maindoc"

tag_schemas_2_1 = {clark_tag("inv:Invoice"): schema_2_1_main / "UBL-Invoice-2.1.xsd"}

ubl_version_finder_xp = UBLXpath("//cbc:UBLVersionID")


def validate(tree: etree._ElementTree, raise_: bool = False) -> bool:
    """Validate an UBL document against its associated schema.

    Args:
        tree: The tree document to validate
        raise_: True to raise an exception if the validation fails

    Returns:
        True if the document is validated (and raise_is False), False

    Raises:
        Validation failure - see https://lxml.de/validation.html#xmlschema
    """
    # We find the appropriate XSD file
    ubl_version = ubl_version_finder_xp(tree)
    if len(ubl_version) > 0:
        ubl_version = ubl_version[0].text.strip()
    else:
        ubl_version = "2.0"
    ubl_version_tuple = tuple([int(x) for x in ubl_version.split(".")])
    if ubl_version_tuple > (2, 1):
        warnings.warn(f"We cannot validate UBL {ubl_version} documents. Trying anyway")

    root = tree.getroot()
    schema = get_schema(root.tag)
    if schema is None:
        if raise_:
            raise KeyError(f"No schema available for root tree {root.tag}")
        return False
    if raise_:
        schema.assertValid(tree)
        return True
    return schema.validate(tree)


@lru_cache(maxsize=4)
def get_schema(tag: str) -> t.Optional[etree.XMLSchema]:
    """Gets and caches the validation schema for a root element

    Args:
        tag: The tag of the root element (clark form)

    Returns:
        A parsed XSD schema or None if not found
    """
    schema_path = tag_schemas_2_1.get(tag)
    if schema_path is None:
        return None
    with open(schema_path, "rb") as stream:
        schema = etree.XMLSchema(file=stream)
    return schema
