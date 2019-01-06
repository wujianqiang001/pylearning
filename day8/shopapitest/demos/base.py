#!/usr/bin/env python
# coding=utf-8
import requests
from .getcase import getdata
def api(trade):
    r1 = requests.get("http://127.0.0.1:5000/gettprice?trade={}".format(trade))
    price = r1.json()
    return price

def api_1():
    r1 = requests.get("http://127.0.0.1:5000/gettrades")
    price = r1.json()
    print(price)

def api_2(trade,unit,exp):
    r = api(trade)
    price = r["data"]
    r1 = requests.get("http://127.0.0.1:5000/gettprices?trade=apple&price={}&unit={}".format(price,unit))
    assert r1.status_code == 200,"status_code: {}".format(r1.status_code)
    prices = r1.json()
    assert str(exp) == prices["data"],"prices is {}".format(prices["data"])
    print(prices)

if __name__ == "__main__":
    # api("pear")
    # api_1()
    exp = 7.1
    api_2("pear","2",exp)