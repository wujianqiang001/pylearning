#!/usr/bin/env python
# coding=utf-8
def fun(a):
    return a+1
f = fun(1)
print(f)

g = lambda x: x+1
f = g(10)
print(f)

int2str = lambda x: str(x)
print(type(int2str(2)))

numadd = lambda x,y: x+y
print(numadd(2,3))



