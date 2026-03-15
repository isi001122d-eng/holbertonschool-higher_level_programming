#!/usr/bin/python3
"""
Məlumatları XML formatına serializasiya və deserealizasiya edən modul
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Python lüğətini XML faylına çevirir
    """
    # Kök (root) element yaradırıq
    root = ET.Element("data")

    # Lüğətin hər bir elementini kök altına əlavə edirik
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # XML ağacını yaradırıq və fayla yazırıq
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    XML faylından məlumatları oxuyur və lüğətə çevirir
    """
    try:
        # XML faylını parse edirik
        tree = ET.parse(filename)
        root = tree.getroot()

        # Elementləri yenidən lüğətə yığırıq
        return {child.tag: child.text for child in root}
    except Exception:
        return None
