#!/usr/bin/env python
# coding=utf-8
#优化代码，函数返回值
def checkphone(phone):
    L = len(phone)
    ps = ["131","132","133","135","136","138","139","180","189"]
    if L == 11:
        if phone.isdigit() == True:
            # if phone[:3] == "138" or phone[:3] == "135" or phone[:3] == "180":
            if phone[:3] in ps:
                return "legal phone"
            else:
                return "illegal phone"
        else:
            return "illegal phone"
    else:
        return "illegal phone"
############################################################################
f = open("phones.txt","r")
for p in f:
    p = p.strip()
    c = checkphone(p)
    print(p+">>>>>"+c)