#!/usr/bin/env python
# coding=utf-8
#手机合法性校验的基础代码
phone = "13811010345"
L = len(phone)
print(L)
ps = ["131","132","133","135","136","139","180","189"]
if L == 11:
    print(phone.isdigit())
    if phone.isdigit() == True:
        print(phone[:3])
        # if phone[:3] == "138" or phone[:3] == "135" or phone[:3] == "180":
        if phone[:3] in ps:
            print("legal phone")
        else:
            print("illegal phone")
    else:
        print("illegal phone")
else:
    print("illegal phone")