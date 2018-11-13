#!/usr/bin/env python
# coding=utf-8
# scort = [4.1, 4.2, 4.4, 3.9, 4.9, 5.0]
# scort.sort()
# print(scort)
# _, *b, _ = scort
# print(b)
# print(sum(b)/len(b))
def fun(*args):
    return args

# print(fun("a", "b", "c", "d", "e", 12, [1,2,3], {"a":"A"}))
def fun1(**kwargs):
    return kwargs

# print(fun1(a="A",b="B"))
def fun2(default = "abc", *args, **kwargs):
    return kwargs, args, default

# print(fun2("a",1,[],a="A",b="B"))

def fun3(a, default = 1.2):
    return a, default
# print(fun3(2, 2.4))

from PR1.day2.shopping import tradeprice, sumprice
def gettradeprice(*args):
    tp = {}
    for trade in args:
        tp[trade] = tradeprice(trade)
    return tp

def getsumprice(**kwargs):
    tp = {}
    for k in kwargs:
        tp[k] = sumprice(k, kwargs[k])
        # print("%s==========%.2f"%(k,sumprice(k, kwargs[k])))
    return tp
# gettradeprice("apple", "pear", "banana", "a")
print(getsumprice(apple=3,pear=5))






