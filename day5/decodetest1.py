#!/usr/bin/env python
# coding=utf-8
def fun1(fun):
    a,b = fun()
    return a+b

@fun1
def fun2():
    return 1, 2

c = fun2
print(c)