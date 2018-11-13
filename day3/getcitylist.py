#!/usr/bin/env python
# coding=utf-8
import requests
import xml.etree.ElementTree as ET
import os,xlsxwriter,xlrd,time
import threading,json,pickle
def loaddatas():
    r = requests.get("http://mobile.weather.com.cn/js/citylist.xml")
    # r.encoding = "utf-8"
    content = r.text
    with open("citylist.xml","w",encoding='UTF-8') as f:
        f.write(content)

def parsedata():
    # xmlFilePath = os.path.abspath("citylist.xml")
    tree = ET.parse("citylist.xml")
    citydatas = []
    # root = tree.getroot()
    # for child in root:
    #     print(child,child.tag,child.attrib,child.text)
    #     for child_child in child:
    #         # print(child_child, child_child.tag, child_child.attrib, child_child.text)
    #         print(child_child.attrib)
    for child in tree.iter(tag='d'):
        data = child.attrib
        if data["d1"].startswith("101"):
            citydatas.append([data["d4"],data["d2"],data["d3"],data["d1"]])
    return citydatas

def writeexcel(datas):
    wk = xlsxwriter.Workbook("citys.xlsx")
    st = wk.add_worksheet()
    st.write(0,0,"省份")
    st.write(0,1,"地市")
    st.write(0,2,"地市名")
    st.write(0,3,"地市编号")
    i = 1
    for data in datas:
        j = 0
        for d in data:
            st.write(i,j,d)
            j += 1
        i += 1

def readexcel():
    rk = xlrd.open_workbook("citys.xlsx")
    st = rk.sheet_by_index(0)
    rows = st.nrows
    citydatas = {}
    for i in range(1,rows):
        city = st.cell(i,0).value
        area = st.cell(i,1).value
        num = st.cell(i,3).value
        citydatas["%s %s"%(city,area)] = num
    return citydatas

def readexcel_p():
    rk = xlrd.open_workbook("citys.xlsx")
    st = rk.sheet_by_index(0)
    rows = st.nrows
    citydatas = {}
    for i in range(1,rows):
        city = st.cell(i,0).value
        area = st.cell(i,1).value
        num = st.cell(i,3).value
        if city not in citydatas:
            citydatas[city] = {area:num}
        else:
            citydatas[city][area] = num
        # print(citydatas)
    return citydatas

def getweather(num):
    try:
        r = requests.get("http://www.weather.com.cn/data/sk/%s.html"%num,timeout=100)
        r.encoding = "utf-8"
        data = r.json()
        d = {}
        d["temp"] = data["weatherinfo"]["temp"]
        d["wind"] = "%s %s"%(data["weatherinfo"]["WD"],data["weatherinfo"]["WS"])
    except:
        d = {}
    # print(d)
    return d

def cityweather(*args):
    nums = readexcel()
    citys = args
    citydatas = {}
    for city in citys:
        num = nums.get(city)
        if num:
            w = getweather(num)
            citydatas[city] = w
        else:
            citydatas[city] = "该地区不存在"
    return citydatas

def citysweater():
    nums = readexcel_p()
    citydatas = {}
    def getcityweather(k,k1,num):
        value = getweather(num)
        citydatas["%s %s"%(k,k1)] = value
    for k,v in nums.items():
        for k1,v1 in v.items():
            # value = getweather(v1)
            # citydatas["%s %s"%(k,k1)] = value
            t = threading.Thread(target=getcityweather,args=(k,k1,v1))
            t.start()
    # return citydatas
    with open("citysweater.txt","w",encoding="utf-8") as f:
        f.write(json.dumps(citydatas))
    # json.dump(citydatas,open("citysweater.txt","w",encoding="utf-8"))
def fun(*args):
    print(args)

def threadtest():
    def fun():
        print("hello")
        time.sleep(3)
    for i in range(5):
        fun()
    print("*"*20)
    for i in range(5):
        t = threading.Thread(target=fun,args=())
        t.start()
def readjson():
    w = json.load(open("citysweater.txt"))
    for k ,v in w.items():
        print(k,v)
if __name__ == "__main__":
    # loaddatas()
    # datas = parsedata()
    # writeexcel(datas)
    # print(readexcel_p())
    # print(getweather("101010700"))
    # print(cityweather("北京 海淀","上海宝山","天津 武"))
    # fun("a","b","c")
    # citysweater()
    # threadtest()
    readjson()