#!/usr/bin/env python
# coding=utf-8
import xlrd
def getdata(pyfile):
    rk = xlrd.open_workbook("testcase/%s.xlsx"%pyfile)
    st = rk.sheet_by_index(0)
    rows = st.nrows
    cols = st.ncols
    data = []
    for i in range(1,rows):
        data_rows = []
        for j in range(cols):
            d = st.cell(i,j).value
            if j == 0:
                if d == "off":
                    break
            data_rows.append(d)
        if data_rows:
            data.append(data_rows)
    return data

if __name__ == "__main__":
    data = getdata()
    print(data)