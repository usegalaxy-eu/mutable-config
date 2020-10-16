#!/usr/bin/env python

# sort tools
# usage: python sort_tools.py in.xml out.xml

import sys

import lxml.etree as le

parser = le.XMLParser(remove_blank_text=True, remove_comments=True)
with open(sys.argv[1], 'r') as f:
    doc = le.parse(f, parser)
    for section in doc.xpath('//section'):
        section[:] = sorted(section, key=lambda x: x.attrib['file'])
    doc.write(sys.argv[2], xml_declaration=True, pretty_print=True)
