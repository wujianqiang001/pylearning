#!/usr/bin/env python
# coding=utf-8
#通过三目运算优化代码
def checkphone(phone):
    L = len(phone)
    ps = ["131","132","133","135","136","138","139","180","189"]
    b = "legal phone" if L == 11 and phone.isdigit() == True and phone[:3] in ps else "illegal phone"
    return b
############################################################################
with open("phones.txt","r") as f, open("report.txt","w",encoding="utf-8") as f1:#with上下文管理
    for p in f:
        p = p.strip()
        c = checkphone(p)
        f1.write("%s>>>>>%s\n"%(p,c))#字符串格式化