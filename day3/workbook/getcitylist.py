# -*- coding:utf-8 -*-
__author__ = 'changhongwei'

import requests,xlsxwriter
from xml.etree import ElementTree as ET

def loaddata():
    r = requests.get(url="http://mobile.weather.com.cn/js/citylist.xml")
    content = r.text
    #with open("citylist.xml","w") as f:
    with open("citylist.xml","w",encoding='UTF-8') as f:
        f.write(content)
        f.close()


# wb = xlsxwriter.Workbook("citylist.xls")
# sh1 = wb.add_worksheet("citylist")

def data_p():
    tree = ET.parse("citylist.xml")
    root = tree.getroot()
    datas = []
    for child in root:
        for children in child:
            a = children.attrib
            if a["d1"].startswith("101"):
                datas.append([a["d4"],a["d3"],a["d2"],a["d1"]])
    return datas


b = data_p()
print(b)