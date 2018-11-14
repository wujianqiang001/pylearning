#!/usr/bin/env python
# coding=utf-8
#学习下字典用法

dic = {"+":"add","-":"div","num":123,"lis":[1,2,3]}
print(dic["+"])
print(dic["num"])
# print(dic["a"])#会报错，因为dic字典中没有键为a
print(dic.get("a"))
print(dic.get("a",1))#字典dic没有a，则返回1，有的话，返回a对应的值
print(dic.get("num",1))#字典dic中有num，返回num对应的值123
dic["b"] = 345#字典dic新增键值对 "b":345
print(dic)

for k,v in dic.items():
    print(k,v)

for k in dic:
    print(k,dic[k])

for v in dic.values():
    print(v)

for k in dic.keys():
    print(k)