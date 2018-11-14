#!/usr/bin/env python
# coding=utf-8
import xlrd
from configparser import ConfigParser
config = ConfigParser()
def getconf():
    config.read("keys.ini")
    key = config.get("key","key")
    return key.split(";")

rd = xlrd.open_workbook("user_session_2018-06-07_suning_smartaudio.xls")
st = rd.sheet_by_name("苏宁智能音箱")
rows = st.nrows
def getcontent():
    for row in range(1,rows):
        content = st.row_values(row)
        yield content
def getkey(key):
    title = st.row_values(0)
    count = title.index(key)
    return count

def getcount():
    keys = getconf()
    count = []
    for k in keys:
        count.append(getkey(k))
    return count

def getdata():
    # key = "uid"
    # key1 = "source_type"
    # key2 = "intent"
    # c = getkey(key)
    # c1 = getkey(key1)
    # c2 = getkey(key2)
    count = getcount()
    content = getcontent()
    datas = {}
    for cont in content:
        keys = []
        for i in count:
            keys.append(cont[i])
        key = tuple(keys)
        datas[key] = cont
        # datas[cont[c]] = cont
    return datas
if __name__ == "__main__":
    d = getdata()
    for k,v in d.items():
        if "FF31F021003A3620FB96053F" in k:
            print(k,v)


