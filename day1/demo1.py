#!/usr/bin/env python
# coding=utf-8
#重点学习列表的可变性，当函数的参数是列表时，需要关注实际参数列表的改变
def fun(a):
    a[0] = "abc"
    return a

lis = ["hello","world"]
lis1 = lis[:]#切片
f = fun(lis1)
print(f)
print(lis)