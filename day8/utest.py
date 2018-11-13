#!/usr/bin/env python
# coding=utf-8
def fun(a):
    try:
        assert 1 == a
        print(".",end=" ")
    except:
        print("F",end=" ")

alist = [1,2,3,4,1,2,1]
for a in alist:
    fun(a)