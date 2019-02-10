"""
=================
ubllib.validation
=================

Validates xml data against schema
"""
from lxml import etree

from . import package_directory
from .namespaces import clark_tag, prefix_ns_map

tag_schemas = {
    'inv:Invoice':  package_directory / 'schemas_3_1'
}

def validate(tree: etree._ElementTree, raise_=False):

    # We determine the applicable schema
    root = tree.getroot()

    # We find the appropriate XSD file
    schema_location = root.attrib[clark_tag('xsi:schemaLocation')]
    ubl_version = tree.xpath('//cbc:UBLVersionID', namespaces=prefix_ns_map)
    # zzz (WIP)
