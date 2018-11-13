#!/usr/bin/env python
# coding=utf-8

def swager(f):
    print("hello")
    return f

def fun(a=None):
    return a or ""

print(swager(fun(1)))

#====================================

def swager(f):
    print("hello")
    return f

@swager
def fun1(a=None):
    return a or ""