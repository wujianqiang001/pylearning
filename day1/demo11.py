#!/usr/bin/env python
# coding=utf-8
#with上下文管理的学习
def checkphone(phone):
    L = len(phone)
    ps = ["131","132","133","135","136","138","139","180","189"]
    if L == 11 and phone.isdigit() == True and phone[:3] in ps:
        return "legal phone"
    return "illegal phone"
############################################################################
with open("phones.txt","r") as f, open("report.txt","w",encoding="utf-8") as f1:#with上下文管理
    for p in f:
        p = p.strip()
        c = checkphone(p)
        f1.write("%s>>>>>%s\n"%(p,c))#字符串格式化
