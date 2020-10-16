#!/usr/bin/env python
# usage: merge_sections.py in.xml out.xml
import sys

import lxml.etree as le

sections = {}

parser = le.XMLParser(remove_blank_text=True, remove_comments=True)
with open(sys.argv[1], 'r') as f:
    doc = le.parse(f, parser)
    for elem in doc.xpath('//section'):
        if elem.attrib['id'] not in sections:
            sections[elem.attrib['id']] = elem
        else:
            tgt = sections[elem.attrib['id']]
            sys.stderr.write("moving from {}:{} to {}:{}\n".format(elem.attrib['id'],
                                                                   elem.attrib['name'], 
                                                                   tgt.attrib['id'],
                                                                   tgt.attrib['name']))
            for t in elem:
                tgt.append(t)
            parent = elem.getparent()
            parent.remove(elem)
    doc.write(sys.argv[2], xml_declaration=True, pretty_print=True)
