#!/usr/bin/env python
# coding=utf-8
import xlrd,xlsxwriter
wk = xlrd.open_workbook("运营数据日报.xlsx")
st = wk.sheet_by_name("接口性能原始数据")
rows = st.nrows
gcdata = {}
for i in range(2,rows):
    gc = st.cell(i,11).value
    dq = st.cell(i,0).value
    s = st.cell(i,2).value
    f = st.cell(i,3).value
    if gc not in gcdata:
        gcdata[gc] = {dq:int(s)+int(f)}
    else:
        if dq not in gcdata[gc]:
            gcdata[gc][dq] = int(s)+int(f)
        else:
            gcdata[gc][dq] += int(s)+int(f)
for k,v in gcdata.items():
    gcdata[k] = sorted(v.items(), key=lambda x:x[1],reverse=True)

workbook = xlsxwriter.Workbook("运营日报1.xlsx")
worksheet = workbook.add_worksheet()
for k,v in gcdata.items():
    if k == "办理":
        row = 2
        for n,s in v:
            worksheet.write(row,3,n)
            worksheet.write(row,4,s)
            row += 1
    if k == "查询":
        row1 = 2
        for n,s in v:
            worksheet.write(row1,0,n)
            worksheet.write(row1,1,s)
            row1 += 1
    if k == "充值":
        row2 = 2
        for n,s in v:
            worksheet.write(row2,6,n)
            worksheet.write(row2,7,s)
            row2 += 1

workbook.close()



