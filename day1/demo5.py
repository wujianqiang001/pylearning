#!/usr/bin/env python
# coding=utf-8
#自动化测试的初接触，文本操作学习
def checkphone(phone):
    L = len(phone)
    ps = ["131","132","133","135","136","138","139","180","189"]
    if L == 11:
        if phone.isdigit() == True:
            # if phone[:3] == "138" or phone[:3] == "135" or phone[:3] == "180":
            if phone[:3] in ps:
                print("legal phone")
            else:
                print("illegal phone")
        else:
            print("illegal phone")
    else:
        print("illegal phone")
############################################################################
f = open("phones.txt","r")
for p in f:
    p = p.strip()
    print(p)
    checkphone(p)