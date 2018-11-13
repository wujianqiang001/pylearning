#coding=utf-8
import xlrd
from htds_interface_agin_test.common.read_config_file  import pro_path
import os
class Data(object):
    def __init__(self,filename):
        filename_dir = os.path.join(pro_path,"data",filename)
        self.wk = xlrd.open_workbook(filename_dir)
    def ReadTestcase(self,sheetname,casename):
        sheet = self.wk.sheet_by_name(sheetname)
        rows = sheet.nrows
        for i in range(1,rows):
            if sheet.cell(i,0).value==casename:
                return sheet.row_values(i)
if __name__ == '__main__':
    data = Data("interface_testcase.xlsx")
    print(data.ReadTestcase("note","test_note_normal"))


