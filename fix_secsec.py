#!/usr/bin/env python
# flatten sections in sections
# usage: python fix_secsec.py in.xml out.xml

import sys

import lxml.etree as le

parser = le.XMLParser(remove_blank_text=True, remove_comments=True)
with open(sys.argv[1], 'r') as f:
    doc = le.parse(f, parser)
    for elem in doc.xpath('//section'):
        parent = elem.getparent()
        if parent.tag != "section":
            continue
        sys.stderr.write("{} -> {}\n".format(elem.attrib, parent.attrib))
        for c in elem:
            parent.append(c)
        parent.remove(elem)
    doc.write(sys.argv[2], xml_declaration=True, pretty_print=True)
