#!/usr/bin/env python
# coding=utf-8
# a = 1.2345678
# b = round(a,4)
# print(b,type(b))
# c = "%.4f"%a
# print(c,type(c))
# a = [] or {} or 1
# print(a)
# d = "h" if not a else "k"
# print(dir(d))
# i = 1.23
# j = "1.34"
# print("jkjkjkj%r jkjkjk %s jkjklkfjafak"%(i,j))
# print("jkjkjkj{a} jkjkjk {b} jkjklkfjafak".format(a=i,b=j))
# intab = "abcd"
# outtab = "1234"
# str_trantab = str.maketrans(intab,outtab)
# print(str_trantab)
# str1 = "this is string example....wow!!!"
# print(str1.translate(str_trantab))
# a = "abcd"
# print(a[1])
# print(a[1:])
# print("b" in a)
# print("b" not in a)
# a = r"ac\n"
# print(a)
# b = "ac\n"
# print(b)
# a = [2]
# b = [1]
# print(a+b)
# print(a*10)
# c = [1,2,3,4,5,6]
# print(c[3])
# print(c[3:])
# print(c[::-1])
# print(c[::2])
# print(dir(c))
# d = c.pop(1)
# print(d)
# a = [1,"a","abc",[1,"a","abc",[1,"a","abc"]],(),{}]
# print(a[3][3][0])
# a = []
# for i in range(2):
#     a.append([])
#     for j in range(2):
#         a[i].append([])
#         for k in range(2):
#             a[i][j].append(k)
# print(a)
# a = (1,2)
# b = (3,4)
# c = a+b
# print(dir(c))
# a = [1,2,3,4,5]
# b = (1,2,3,4,5)
# a[0] = 2
# # b[0] = 2
# print(a)
# print(b)
# c = ([1,2,3],4)
# c[0][0] = 2
# print(c)
a = {"a":1,"b":2,"c":3}
for k in a:
    print(k,a[k])
for k,v in a.items():
    print(k,v)

b = {}
import os