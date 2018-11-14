#!/usr/bin/env python
# coding=utf-8
from datetime import datetime
def getymd():
    y = datetime.now().year
    m = datetime.now().month
    d = datetime.now().day
    return y,m,d#返回元祖格式

def leapyear(year):
    if (not year%4 and year%100) or not year%400:
        return True
    else:
        return False

def idnumcheck(idnum):
    if len(idnum) == 18 and (idnum.isdigit() or (idnum[-1] == "X" and idnum[:-1].isdigit())):
        return True
    return False

def getidymd(idnum):
    if idnumcheck(idnum):
        return int(idnum[6:10]),int(idnum[10:12]),int(idnum[12:14])
    return False

def checkymd(idnum):
    if not getidymd(idnum):
        return False
    y,m,d = getidymd(idnum)
    y1,m1,d1 = getymd()
    if y > y1 or y < y1-100:
        return False
    if m > 12 or m < 1:
        return False
    if y == y1 and m > m1:
        return False
    if m == m1 and d > d1:
        return False
    if m == 2:
        if leapyear(y):
            if d > 29:
                return False
        else:
            if d> 28:
                return False
    if m in [1,3,5,7,8,10,12]:
        if d > 31:
            return False
    else:
        if d > 30:
            return False
    if y == 0 or m == 0 or d == 0:
        return False
    return True

def main(idnum):
    if checkymd(idnum):
        print("%s is legal ID number!"%idnum)
    else:
        print("%s is illegal ID number!"%idnum)

def idunmbertest(idnum):
    if checkymd(idnum):
        return 1
    else:
        return 0

if __name__ == "__main__":
    Id = "11010818880129951X"
    main(Id)