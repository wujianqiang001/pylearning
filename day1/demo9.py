#!/usr/bin/env python
# coding=utf-8
def fun():
    "无参数无返回值"
    print(1+2)

def fun1(a,b):
    "有参数无返回值"
    print(a+b)

def fun2():
    "无参数有返回值"
    return 1+2

def fun3(a,b):
    "有参数有返回值"
    return a+b

def pf(a):
    print(a*20)

a = 123
print(a)
pf("*")
b= "hello"
print(b)
pf("+")
c = [1,2,3]
print(c)
pf("=")

def fun4(a):
    "根据参数值，决定了该函数是有返回，还是无返回"
    if a<10:
        return "a"

f = fun4(50)
print(f)

def fun5(a):
    if a<10:
        return "a"
    return "b"

f = fun5(50)
print(f)