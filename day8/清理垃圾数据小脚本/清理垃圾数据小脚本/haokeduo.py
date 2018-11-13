# -*- coding: gbk -*-
def ReadRow():
    '''
    #读测试数据
    #方法一
    # L = []
    # with open('test.txt','r') as f:
    #     f=f.decode()
    #     for line in f.readlines():
    #         L.append(line.strip('\n'))
    '''

    # 读测试的数据
    # 方法二
    import xlrd, xlwt  # 导入读写模块
    wbk = xlrd.open_workbook(u'Testdata2.xls')  # 打开过滤文件
    SheetName = wbk.sheet_names()  # 获取工作表名字
    l = []
    L = []
    for sheet_name in SheetName:
        SheetRow = wbk.sheet_by_name(sheet_name)  # 获取工作表行
        TableRow = SheetRow.nrows, SheetRow.ncols  # 统计工作表行数
        for i in range(TableRow[0]):  # 循环每一行
            Rows1 = SheetRow.row_values(i)  # 获取第一行
            l.append(Rows1)  # 追加到空列表
        break
    for z in l:#循环列表
        for q in range(TableRow[1]):
            L.append(z[q])

    # 读需要修改的数据
    workbook1 = xlrd.open_workbook(u'haokeduo.xls')  # 打开文件
    sheet_names = workbook1.sheet_names()  # 打开的工作表名字
    row_list = []#定义空列表
    L = [x for x in L if x != '']  # 更新列表，删除空字符串
    for sheet_name in sheet_names:
        sheet2 = workbook1.sheet_by_name(sheet_name)  # 获取工作表行
        table = sheet2.nrows, sheet2.ncols  # 统计工作表行数
        wb = xlwt.Workbook()  # 打开新excel
        ws = wb.add_sheet(u'好课多导出结果')  # 工作表名更名
        for i in range(table[0]):  # 循环每一行
            rows1 = sheet2.row_values(i)  # 获取第一行内
            union = list(set(L) & set(rows1))  # 取两个列表的交集
            if union:  # 判断交集是否为真
                continue  # 跳过
            else:
                row_list.append(rows1)  # 追加到空列表
        break

    # 重新写过滤后的数据
    w = 0  # 定义新excel的行初始值
    for z in row_list:  # 循环把列表内容赋值给变量
        for q in range(table[1]):  # 获取每列
            if type(z[q]) == float:  # 判断列的值是否为浮点型
                ws.write(w, q, int(z[q]))  # 转换成整型
            else:
                ws.write(w, q, str(z[q]))  # 直接写到单元格

        w += 1  # 行数+1
    wb.save('XGhaokeduo.xls')#保存为新的文件


def SJ():#封装的查看运行时间
    import time
    start = time.time()
    ReadRow()
    end = time.time()
    print(end - start)


SJ()
