#!/usr/bin/env python
# coding=utf-8

import os,sys
print(sys.path)
if __name__ == "__main__":
    pyfile = os.path.basename(sys.argv[0])
    os.system("pytest testsuite -s --alluredir reports/allure-report")
    os.system("allure serve -h 127.0.0.1 -p 8001 reports/allure-report")