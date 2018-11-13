#!/usr/bin/env python
# coding=utf-8

def fun1(fun):
    def _dec(a):
        print("="*20)
        b = fun(a)
        print("="*20)
        return a
    return _dec

def fun11(fun):
    print("*"*20)
    fun()
    print("*"*20)
    return fun

@fun1
def fun2(a):
    print (a)

# @fun11
# def fun3():
#     print("my god")
#fun2(110)



