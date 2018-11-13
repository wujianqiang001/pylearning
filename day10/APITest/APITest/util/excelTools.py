# -*- coding:utf-8 -*-
'''
excel处理  问题：读取excel数据从第二行，如果用循环会下标越界 if i != rows-1:这个判断合理吗
'''
import xlsxwriter,xlrd
from APITest.util.tools import *

#获取API列表
def getAPIList(address):
    workbook = xlrd.open_workbook(address)
    worksheet = workbook.sheet_by_name("API")
    rows = worksheet.nrows
    api_values = []
    for i in range(rows):
        if i != rows-1:
            value = worksheet.cell(i+1,1).value
            api_values.append(value)
    return api_values

#获取excel用例整行信息封装成列表
def getCaseInfo(address):
    workbook = xlrd.open_workbook(address)
    worksheet = workbook.sheet_by_name("API")
    rows = worksheet.nrows
    infoList = []
    for i in range(rows):
        if i != rows-1:
            swtich = worksheet.cell_value(i+1,0)
            url = worksheet.cell_value(i+1,1)
            header = worksheet.cell_value(i+1,4)
            body = worksheet.cell_value(i+1,5)
            method = worksheet.cell_value(i+1,6)
            expect_code = worksheet.cell_value(i+1,7)
            expect_content = worksheet.cell_value(i+1,8)
            #print(swtich,url,header,body,method,expect_code,expect_content)
            info = {"swtich":swtich,"url":url,"header":header,"body":body,"method":method,"expect_code":expect_code,"expect_content":expect_content,"row":i}
            infoList.append(info)
    return infoList

#向excel中输入结果
def writeExcel():
    pass



if __name__ == "__main__":
    address = readConfig("../config/config.ini","excel","address")
    print(getCaseInfo(address))
