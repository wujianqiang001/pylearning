#!/usr/bin/env python
# coding=utf-8
import xlrd,sys,os
filepath = os.path.dirname(sys.argv[0])
def getdata(file):
    wk = xlrd.open_workbook(file)
    sheet = wk.sheet_by_index(0)
    rows = sheet.nrows
    testcase = []
    for i in range(1,rows):
        switch = sheet.cell(i,0).value
        url = sheet.cell(i,1).value
        flag = sheet.cell(i,2).value
        assertbody = sheet.cell(i,3).value
        if switch == True:
            testcase.append({"url":url,"flag":flag,"assertbody":assertbody})
    return testcase

if __name__ == "__main__":
    data = getdata("../testcases/testcase.xlsx")
    print(data)