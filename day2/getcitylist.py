#!/usr/bin/env python
# coding=utf-8
import requests
import xml.etree.ElementTree as ET
import os
def loaddatas():
    r = requests.get("http://mobile.weather.com.cn/js/citylist.xml")
    content = r.text
    with open("citylist.xml","w",encoding='UTF-8') as f:
        f.write(content)

def parsedata():
    xmlFilePath = os.path.abspath("citylist.xml")
    tree = ET.parse(xmlFilePath)
    root = tree.getroot()
    # for child in root:
    #     print(child,child.tag,child.attrib,child.text)
    #     for child_child in child:
    #         # print(child_child, child_child.tag, child_child.attrib, child_child.text)
    #         print(child_child.attrib)
    for child in tree.iter(tag='d'):
        print(child.attrib)

if __name__ == "__main__":
    # loaddatas()
    parsedata()