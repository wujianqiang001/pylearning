#!/usr/bin/env python
# coding=utf-8
import requests,json
from PR1.day11.com.gettoken import *
from configparser import ConfigParser
conf = ConfigParser()
conf.read("config/config.ini")
env = conf.get("env","env")
if env == "pre":
    host = conf.get("pre","url")
if env == "test":
    host = conf.get("test","url")
uuid,login_token = token()
def request(method,uri,header,body):
    if header:
        header = json.loads(header)
    else:
        header = None
    body = json.loads(body)
    body["uuid"] = uuid
    body["login_token"] = login_token
    if method == "get":
        r = requests.get("http://%s%s"%(host,uri),params=body,headers=header)
    if method == "post":
        r = requests.post("http://%s%s"%(host,uri),json=body,headers=header)
    return r