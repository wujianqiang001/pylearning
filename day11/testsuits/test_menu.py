#!/usr/bin/env python
# coding=utf-8
from PR1.day11.com.getdata import *
from PR1.day11.com.request import *
from PR1.day11.com.checkdata import *
import json,pytest,os,allure,sys
pyfile = os.path.split(__file__)[-1].split('.')[0]
data = getdata(pyfile)
@allure.feature("测试模块_meitu")           # 功能块，feature功能分块时比story大,即同时存在feature和story时,feature为父节点
@allure.story("测试模块_menu")             # 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
@allure.issue("BUG号：123")                 # 问题表识，关联标识已有的问题，可为一个url链接地址
@allure.testcase("用例名：订单查询类")
@pytest.mark.parametrize("_,testcase,method,uri,header,body,exception",data,ids=[a[1] for a in data])
def test_main_menu(_,testcase,method,uri,header,body,exception):
    allure.attach("测试用例",testcase)
    r = request(method,uri,header,body)
    allure.attach("请求url",r.url)
    content = r.json()
    exception = json.loads(exception)
    check(exception,content)