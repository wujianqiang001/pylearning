#!/usr/bin/env python
# coding=utf-8
import os,time
t = str(time.time())
if __name__ == "__main__":
    os.system("python3 -m pytest testsuits --alluredir reports\\allure-report-%s"%t)
    # os.system("allure serve reports\\allure-report-%s"%t)
