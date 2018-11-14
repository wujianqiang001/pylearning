#!/usr/bin/env python
# coding=utf-8
import xlrd
def getxlsx():
    wk = xlrd.open_workbook("srcdata/user_session_2018-06-07_suning_smartaudio.xls")
    st = wk.sheet_by_name("苏宁智能音箱")
    rows = st.nrows
    # print(rows)
    for row in range(1,rows):
        # content = st.cell(row,5).value
        content = st.row_values(row)
        yield content

if __name__ == "__main__":
    gx = getxlsx()
    for g in gx:
        print(g)