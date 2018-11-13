#!/usr/bin/env python
# coding=utf-8
import requests,json,pytest,platform
if platform.python_version()[0] == "3":
    from day8.apiTest.baseconfig import *
    from day8.apiTest.com.getmd import getmd
    from day8.apiTest.com.request import *
    from day8.apiTest.com.readexcel import *
    from day8.apiTest.com.assertbody import *
else:
    from baseconfig import *
    from com.getmd import getmd
    from com.request import *
    from com.readexcel import *
    from com.assertbody import *
datas = getdata("testcases/testcase.xlsx")
if pre:
    ip = pre_ip
if test:
    ip = test_ip
@pytest.mark.parametrize("url,flag,assertbody",
                         datas)
def test_case(url,flag,assertbody):
    uri = url
    url = "https://%s%s"%(ip,uri)
    if flag == "args":
        key = key
        auth = getmd("1234"+key)
        r = get(url%auth)
        print(r[0])
        print(r[1])
    elif flag == "header":
        header = header
        r = get(url=url,headers=header)
        print(r[0])
        if assertbody == "content":
            assertbody(r[1],header)
        else:
            print(r[1])

# r = get("https://www.zhihu.com/api/v4/me?include=following_question_count",headers=header)
# print(r[0])
# content = r[1]
# name = json.loads(content)["name"]
# assert name == "03cm"
# print("pass")
#
# r = get("https://www.zhihu.com/api/v4/notifications/v2/default",headers=header)
# print(r[0])
# content = r[1]
# _list = json.loads(content)["data"]
# for i in range(len(_list)):
#     print(i)
#     name_list = _list[i]["content"]["actors"]
#     if isinstance(name_list,list):
#         for j in range(len(name_list)):
#             name = name_list[j]["name"]
#     else:
#         name = _list[i]["content"]["actors"]["name"]
#     print(name)

