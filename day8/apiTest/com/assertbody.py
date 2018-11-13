#!/usr/bin/env python
# coding=utf-8
import json,platform
if platform.python_version()[0] == "3":
    from day8.apiTest.com.request import *
else:
    from request import *
def assertbody(r,header):
    links = []
    content = r
    _list = json.loads(content)["data"]
    for i in range(len(_list)):
        name_list = _list[i]["content"]["actors"]
        if isinstance(name_list,list):
            for j in range(len(name_list)):
                name = name_list[j]["link"]
        else:
            name = _list[i]["content"]["actors"]["link"]
        links.append(name)
    for link in links:
        print(link)
        r1 = get(link,headers=header)
        assert r1[0] == 200
        print("pass")