#!/usr/bin/env python
# coding=utf-8
from shopping import *
a = gettrade()[0]
b = tradeprice_1(a)
s = sumprice(a, 3)
print orderid(a, "tom", "sh")
print orders(a, 3, 1, "tom", "sh")

