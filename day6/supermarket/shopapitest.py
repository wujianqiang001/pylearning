#!/usr/bin/env python
# coding=utf-8
import requests

def api(trade):
    body = {"trade": trade}
    r1 = requests.get("http://127.0.0.1:5000/gettprice?trade=%(trade)s"%body)
    price = r1.text
    body["price"] = price
    body["unit"] = 3
    r2 = requests.get("http://127.0.0.1:5000/gettprices?trade=%(trade)s&price=%(price)s&unit=%(unit)d"%body)
    print(r2.text)

if __name__ == "__main__":
    trade = "apple"
    api(trade)

