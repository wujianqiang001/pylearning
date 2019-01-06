#!/usr/bin/env python
# coding=utf-8
import requests,json
import pytest,allure
from common.getcase import getdata
from ConfigParser import ConfigParser
conf = ConfigParser()
conf.read("configs/config.ini")
ip = conf.get("test","ip")
port = conf.get("test","port")
def getprice(trade):
    r1 = requests.get("http://{}:{}/gettprice?trade={}".format(ip,port,trade))
    price = r1.json()
    return price
datas = getdata()
@allure.feature("模块1")
@allure.story("功能1")
@pytest.mark.parametrize("case,uri,param,exp",
                         datas,
                         ids=[a[0] for a in datas])
def test_getprices(case,uri,param,exp):
    url = "http://{}:{}{}".format(ip,port,uri)
    param = json.loads(param)
    trade = param["trade"]
    price = getprice(trade)["data"]
    param["price"] = price
    allure.attach("price",price)
    url = url + "?trade={trade}&price={price}&unit={unit}".format(**param)
    r = requests.get(url=url)
    assert r.status_code == 200,"status_code: {}".format(r.status_code)
    assert r.json()["data"] == str(exp),"price: {}".format(r.json()["data"])
