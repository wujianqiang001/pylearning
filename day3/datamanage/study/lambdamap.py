#!/usr/bin/env python
# coding=utf-8
# m = map(str,range(10))
# for m1 in m:
#     print(m1,type(m1))

f = lambda a:a+1
d = [1,2,3]
f1 = map(f,d)
a,b,c = f1
print(a,b,c)
