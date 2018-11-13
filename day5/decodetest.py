#!/usr/bin/env python
# coding=utf-8
# def fun1():
#     print("aaaaaa")
#
# def fun2(fun):
#     fun()
#
# fun2(fun1)

def fun2():
    return 1, 2

def fun1(fun):
    a,b = fun()
    return a+b

c = fun1(fun2)
print(c)
