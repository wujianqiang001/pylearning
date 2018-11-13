import xlrd

def readexcel(file):
    # filecase = r"testcase/apitest.xlsx"
    rk = xlrd.open_workbook(file)
    st = rk.sheet_by_index(0)
    rows = st.nrows
    cases = []
    for i in range(1,rows):
        switch = st.cell_value(i,0)#
        testcase = st.cell_value(i,1)
        method = st.cell_value(i,2)
        url = st.cell_value(i,3)
        body = st.cell_value(i,4)
        expection = st.cell_value(i,5)
        if switch == "on":
            cases.append((testcase, method, url, body, expection))
    return cases
if __name__ == '__main__':
    print(readexcel())