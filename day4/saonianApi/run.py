#!/usr/bin/env python
# coding=utf-8
from PR2.day4.saonianApi.readcase import *
from PR2.day4.saonianApi.gettoken import *
from PR2.day4.saonianApi.request import *
import json
from configparser import ConfigParser
conf = ConfigParser()
conf.read("config.ini")
env = conf.get("env","env")
if env == "preenv":
    host = conf.get("preenv","host")
if env == "testenv":
    host = conf.get("testenv","host")
cases = readexcel()
uuid,login_token = token()
def test_main():
    for case in cases:
        body = json.loads(case["body"])
        body["uuid"] = uuid
        if body.get("login_token"):
            body["login_token"] = login_token
        url = "http://%s"%host+case["url"]
        expection = json.loads(case["expection"])
        method = case["method"]
        request(method,url,body,expection)

if __name__ == "__main__":
    test_main()