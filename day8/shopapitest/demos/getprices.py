#!/usr/bin/env python
# coding=utf-8
import requests,json
from getcase import getdata

ip = "127.0.0.1"
port = "5000"
def getprice(trade):
    r1 = requests.get("http://127.0.0.1:5000/gettprice?trade={}".format(trade))
    price = r1.json()
    return price

def getprices(case,uri,param,exp):
    url = "http://{}:{}{}".format(ip,port,uri)
    param = json.loads(param)
    trade = param["trade"]
    price = getprice(trade)["data"]
    param["price"] = price
    url = url + "?trade={trade}&price={price}&unit={unit}".format(**param)
    r = requests.get(url=url)
    print(r.json())

def main():
    datas = getdata()
    for case,uri,param,exp in datas:
        getprices(case,uri,param,exp)

if __name__ == "__main__":
    main()