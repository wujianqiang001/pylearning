#!/usr/bin/env python
# coding=utf-8
import pytest
import os,sys
module = []
with open("configs/module.txt") as f:
    for line in f:
        if not line.startswith("#"):
            module.append(line.strip())
m = " or ".join(module)

pytest.main(["testsuite/","--alluredir=reports/allure-report"])
# pytest.main(["testsuite/","--html","report/report.html","--alluredir=reports/allure-report"])
os.system("allure serve reports/allure-report")