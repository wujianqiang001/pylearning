import os,sys
print(sys.path)
if __name__ == "__main__":
    pyfile = os.path.basename(sys.argv[0])#系统执行当前文件的路径
    os.system("pytest testsuite -s --alluredir reports/allure-report")#利用pytest运行代码
    os.system("allure serve -h 127.0.0.1 -p 8001 reports/allure-report")#访问本地报告模板
