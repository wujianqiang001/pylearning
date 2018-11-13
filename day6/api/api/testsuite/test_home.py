from api.com.readcase import *
from api.com.gettoken import *
from api.com.request import *
from configparser import ConfigParser
import json,pytest,os,allure

conf =ConfigParser()
conf.read("config/config.ini")
env = conf.get("env","env")
if env == "preenv":
    host = conf.get("preenv","host")
if env == "testenv":
    host = conf.get("testenv","host")
if env == "xxzhcs":
    host = conf.get("xxzhcs","host")
file = r"testcase/apihome.xlsx"
cases = readexcel(file)
uuid,login_token = token()
@allure.feature("测试模块_demo1")           # 功能块，feature功能分块时比story大,即同时存在feature和story时,feature为父节点
@allure.story("测试模块_demo2")             # 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
@allure.issue("BUG号：123")                 # 问题表识，关联标识已有的问题，可为一个url链接地址
@allure.testcase("用例名：首页")
@pytest.mark.parametrize("testcase,method,url,body,expection",cases,ids=[a[0] for a in cases])
def test_main(testcase,method,url,body,expection):
    paras = vars()
    allure.environment(host=host, test_vars=paras)
    allure.attach("测试用例",testcase)
    url = "http://%s"%host+url
    expection = json.loads(expection)
    method = method
    r = request(method,url,body,expection)
    allure.attach("状态码",str(r.status_code))
