#!/usr/bin/env python
# coding=utf-8
import requests
def fun(*args,**kwargs):
    a = args
    b = kwargs
    for i in a:
        print(i)

    for k,v in b.items():
        print(k,v)

def swager(f):
    print("hello")
    return f

@swager
def fun1(a=None):
    return a or ""


if __name__ == "__main__":
    # fun("a","b","c","abc",a=1,b=2)
    print(type(fun1()))