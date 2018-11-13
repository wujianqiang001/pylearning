#!/usr/bin/env python
# coding=utf-8
from PR2.day5.saonianApi.com.readcase import *
from PR2.day5.saonianApi.com.gettoken import *
from PR2.day5.saonianApi.com.request import *
import json,pytest,os,sys,allure
from ConfigParser import ConfigParser
conf = ConfigParser()
conf.read("config/config.ini")
env = conf.get("env","env")
if env == "preenv":
    host = conf.get("preenv","host")
if env == "testenv":
    host = conf.get("testenv","host")
cases = readexcel()
uuid,login_token = token()
# def test_main():
#     for case in cases:
#         body = json.loads(case["body"])
#         body["uuid"] = uuid
#         if body.get("login_token"):
#             body["login_token"] = login_token
#         url = "http://%s"%host+case["url"]
#         expection = json.loads(case["expection"])
#         method = case["method"]
#         request(method,url,body,expection)
@allure.feature("测试模块_demo1")           # 功能块，feature功能分块时比story大,即同时存在feature和story时,feature为父节点
@allure.story("测试模块_demo3")             # 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
@allure.issue("BUG号：123")                 # 问题表识，关联标识已有的问题，可为一个url链接地址
@allure.testcase("用例名：订单查询")
@pytest.mark.parametrize("testcase,method,url,body,expection",
                         cases,
                         ids=[a[0] for a in cases])
def test_main(testcase,method,url,body,expection):
    paras = vars()
    allure.environment(host=host, test_vars=paras)
    allure.attach("测试用例",testcase)
    body = json.loads(body)
    body["uuid"] = uuid
    if body.get("login_token"):
        body["login_token"] = login_token
    url = "http://%s"%host+url
    expection = json.loads(expection)
    method = method
    r = request(method,url,body,expection)
    allure.attach("状态码",str(r.status_code))