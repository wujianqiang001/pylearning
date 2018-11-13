#!/usr/bin/env python
# coding=utf-8

def f(a):
    for i in range(a):
        yield i

def g(a):
    b = []
    for i in range(a):
        b.append(i)
    return b
a = f(10)
b = g(10)
print(type(a))
print(type(b))
print(a)
print(b)
# for k in a:
#     print(k)
#
# for m in b:
#     print(m)

