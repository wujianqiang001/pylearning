#!/usr/bin/env python
# coding=utf-8
from configparser import ConfigParser
import sys,logging
import xlrd,xlsxwriter
logging.basicConfig(level=logging.ERROR,
                    filename="access.log",
                    format='%(asctime)s-%(levelname)s::%(message)s')
def getconfig():
    config = ConfigParser()
    config.read("config.ini")
    key = config.get("key","key")
    title = config.get("title","title")
    fromfile = config.get("fromfile","file")
    fromsheet = config.get("fromsheet","sheet")
    tofile = config.get("tofile","file")
    tosheet = config.get("tosheet","sheet")
    return key,title,fromfile,fromsheet,tofile,tosheet

def getalldatas():
    fromfile, fromsheet = getconfig()[2:4]
    try:
        rd = xlrd.open_workbook(fromfile)
    except:
        logging.error("this file (%s) is no exits"%fromfile)
        sys.exit(0)
    try:
        st = rd.sheet_by_name(fromsheet)
    except:
        logging.error("this sheet (%s) is no exits"%fromsheet)
        sys.exit(0)
    rows = st.nrows
    titles = st.row_values(0)
    datas = []
    for row in range(1,rows):
        values = st.row_values(row)
        datas.append(values)
    return titles, datas

def parserdata():
    key, title = getconfig()[:2]
    titles, datas = getalldatas()
    key = key.split(";")
    title = title.split(";")
    key_index = []
    for k in key:
        if k in titles:
            key_index.append(titles.index(k))
        else:
            logging.error("this key (%s) is no exits"%k)
            sys.exit(0)
    title_index = []
    for t in title:
        if t in titles:
            title_index.append(titles.index(t))
        else:
            logging.error("this title (%s) is no exits"%t)
            sys.exit(0)
    todatas = {}
    for data in datas:
        k = tuple([data[i] for i in key_index])
        v = [data[i] for i in title_index]
        todatas.setdefault(k,[]).append(v)
        # todatas.setdefault(tuple([data[i] for i in key_index]),[]).append([data[i] for i in title_index])
    return todatas

def writedata():
    tofile,tosheet = getconfig()[-2:]
    wk = xlsxwriter.Workbook(tofile)
    wt = wk.add_worksheet(tosheet)
    datas = parserdata()
    title = getconfig()[1]
    title = title.split(";")
    title.append("count")
    j = 0
    for t in title:
        wt.write(0,j,t)
        j += 1
    i = 1
    for v in datas.values():
        wt.write_row(i,0,v[0])
        wt.write(i,len(v[0]),len(v))
        i += 1
    wk.close()

if __name__ == "__main__":
    writedata()
