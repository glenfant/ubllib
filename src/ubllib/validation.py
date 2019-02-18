"""
=================
ubllib.validation
=================

Validates xml data against schema
"""
from functools import lru_cache
import pathlib
import warnings

from lxml import etree

from . import package_directory
from .namespaces import clark_tag, prefix_ns_map

schema_2_1_main = package_directory / 'schemas_2_1' / 'maindoc'

tag_schemas_2_1 = {
    clark_tag('inv:Invoice'): schema_2_1_main / 'UBL-Invoice-2.1.xsd'
}


def validate(tree: etree._ElementTree, raise_=False) -> bool:
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
    ubl_version = tree.xpath('//cbc:UBLVersionID', namespaces=prefix_ns_map)
    if len(ubl_version) > 0:
        ubl_version = ubl_version[0].text.strip()
    else:
        ubl_version = '2.0'
    ubl_version_tuple = tuple([int(x) for x in ubl_version.split('.')])
    if ubl_version_tuple > (2, 1):
        warnings.warn(f"We cannot validate UBL {ubl_version} documents. Trying anyway")

    root = tree.getroot()
    schema_path = tag_schemas_2_1[root.tag]
    schema = get_schema(schema_path)
    if raise_:
        schema.assertValid(tree)
    else:
        return schema.validate(tree)


@lru_cache(maxsize=4)
def get_schema(path: pathlib.Path) -> etree.XMLSchema:
    """Gets and caches the validation schema from a file

    Args:
        path: Absolute path to the XSD file

    Returns:
        A parsed XSD schema
    """
    with open(path, 'rb') as stream:
        tree = etree.parse(stream)
    schema = etree.XMLSchema(tree)
    return schema
