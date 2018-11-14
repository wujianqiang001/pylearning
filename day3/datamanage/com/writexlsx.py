#!/usr/bin/env python
# coding=utf-8
import xlsxwriter

def writedata(kwargs):
    wk = xlsxwriter.Workbook("resultdata/user.xlsx")
    for sheet,data in kwargs.items():
        st = wk.add_worksheet(sheet)
        row = 0
        for c in data:
            st.write_row(row,0,c)
            row += 1
    wk.close()



