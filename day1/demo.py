#!/usr/bin/env python
# coding=utf-8
#斐波那契数列的实现方式，重点深入学习列表索引在实际案例中的使用
a = [0,1]#变量a,赋值[0,1],列表
for i in range(10):
    print(a)
    a.append(a[-1]+a[-2])

print(a)