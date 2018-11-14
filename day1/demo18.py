#!/usr/bin/env python
# coding=utf-8
#通过while循环实现斐波那契数列
#重点学习while循环，自增赋值
i = 0
j = 1
L = [0,1]
k = 0
while k < 10:
    m = i + j
    i = j
    j = m
    L.append(m)
    k += 1#自增赋值

print(L)

k = 0
while k<10:
    print(k)
    k = k + 1#k += 1
