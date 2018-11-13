#!/usr/bin/env python
# coding=utf-8
def register():
    while True:
        tel = raw_input("Please input your phoneno:")
        if not checkphone(tel):
            print "Your phoneno is valide"
        else:
            break
    while True:
        pwd = raw_input("Please input your pwd:")
        if not checkpwd(pwd):
            print "Your pwd is valide"
        else:
            break
    while True:
        vc = verificationCode()
        print vc
        vc1 = raw_input("Please input this verficationCode:")
        if vc != vc1:
            print "Your verficationCode is error"
        else:
            break
    return {"code":0, "msg":"sucess", "tel":tel, "pwd":pwd}

def verificationCode():
    import random, string
    a = string.ascii_lowercase + string.digits
    return "".join(random.sample(a, 6))

def checkphone(tel):
    phoneNo = ["131", "132", "133", "134", "135", "136", "137", "138", "139", "180", "188", "189"]
    if tel.isdigit() and len(tel) == 11:
        if tel[0:3] in phoneNo:
            return True
    return False

def checkpwd(pwd):
    import string
    a = string.ascii_letters + "_"
    if pwd[0] in a and 8<=len(pwd)<=20:
        return True
    return False

if __name__ == "__main__":
    print register()
    import xlrd