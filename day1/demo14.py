#!/usr/bin/env python
# coding=utf-8
#通过循环实现斐波那契数列
#重点学习替换赋值
i = 0
j = 1
L = [0,1]
for k in range(10):
    print("before:i=%d"%i)
    print("before:j=%d"%j)
    m = i + j
    i = j
    j = m
    print("m=%d"%m)
    print("end:i=%d"%i)
    print("end:j=%d"%j)
    L.append(m)

print(L)