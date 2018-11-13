#!/usr/bin/env python
# coding=utf-8
import xlrd,xlsxwriter
from configparser import ConfigParser
wk = xlrd.open_workbook("user_session_2018-06-07_suning_smartaudio.xls")
st = wk.sheet_by_index(0)
st1 = wk.sheet_by_name("苏宁智能音箱")
rows = st1.nrows
def switchdata(sdata):
    data = dict(sdata)
    for d in data:
        # data[d] = True if data[d] == "True" else False
        if data[d] == "True":
            data[d] = True
        else:
            data[d] = False
    return data
def switchdata1(sdata):
    data = {}
    for k,v in sdata:
        data[k] = True if v == "True" else False
    return data
def readconfig(item):
    conf = ConfigParser()
    conf.read("config.ini")
    # wbasedata = conf.get("weather","天气")
    wbasedata = conf.items(item)
    return wbasedata
def datap(basedata):
    datas = []
    for i in range(1,rows):
        data = st1.cell(i,5).value
        for d in basedata:
            if basedata[d] and d in data:
                datas.append(data)
                break
    sdata = []
    for data1 in datas:
        for d in basedata:
            if not basedata[d] and d in data1:
                sdata.append(data1)
                break
    return list(set(datas)-set(sdata))
def datap1(basedata,data):
    flag = False
    for d in basedata:
        if basedata[d] and d in data:
            flag = True
            break
    for d in basedata:
        if not basedata[d] and d in data:
            flag = False
            break
    return flag

def readx(basedata):
    # wbasedata = {"天气":True,"温度":True,"热":True,"雨":True,"度":True,"雨伞":True,"伞":True,"百度":False,"辅食":False,"度秘":False}
    # tbasedata = {"几点":True,"分钟":True,"小时":True}
    datas = []
    for i in range(1,rows):
        data = st1.cell(i,5).value
        if datap1(basedata,data):
            datas.append(st1.row_values(i))
    return datas
    # with open("sdata.txt") as f:
    #     for line in f:
    #         line = line.strip()
    #         if datap1(cbasedata,line):
    #             print(line)
    # print("================================================")
def main():
    wbasedata = switchdata(readconfig("weather"))
    tbasedata = switchdata(readconfig("time"))
    cbasedata = switchdata(readconfig("cal"))
    trbasedata = switchdata(readconfig("translate"))
    # readx(wbasedata)
    # readx(tbasedata)
    # readx(cbasedata)
    print(readx(trbasedata))
def writeexecl(rk,sheet,datas):
    rt = rk.add_worksheet(sheet)
    for i in range(len(datas)):
        for j in range(len(datas[i])):
            rt.write(i,j,datas[i][j])

def main1():
    conf = ConfigParser()
    conf.read("config.ini")
    items = conf.sections()
    rk = xlsxwriter.Workbook("users.xlsx")
    for item in items:
        basedata = switchdata(readconfig(item))
        datas = readx(basedata)
        writeexecl(rk,item,datas)
    rk.close()

if __name__ == "__main__":
    main()
    # writeexecl()
