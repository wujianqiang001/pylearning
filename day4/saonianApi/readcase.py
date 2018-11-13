#!/usr/bin/env python
# coding=utf-8
import xlrd
def readexcel():
    rk = xlrd.open_workbook("testcase.xlsx")
    st = rk.sheet_by_index(0)
    rows = st.nrows
    cases = []
    for i in range(1,rows):
        switch = st.cell(i,0).value
        testcase = st.cell(i,1).value
        method = st.cell(i,2).value
        url = st.cell(i,3).value
        body = st.cell(i,4).value
        expection = st.cell(i,5).value
        if switch == "on":
            cases.append({"testcase":testcase,"method":method,"url":url,"body":body,"expection":expection})
    return cases