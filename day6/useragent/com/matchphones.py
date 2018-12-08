#!/usr/bin/env python
# coding=utf-8
import re,os
def writelog(data):
    with open("../phones/phones.log","a") as f:
        f.write(data+"\n")
def matchua():
    with open("../sourcedata/uadatas.log") as f:
        for line in f:
            phone = re.search("[\dn];\s?(.+)\sBuild",line.strip())
            if phone:
                p = phone.groups()[0]
                ph = re.search("[sn];\s(.+)",p)
                if ph:
                    pho = ph.groups()[0]
                    writelog(pho)
                else:
                    writelog(p)

if __name__ == "__main__":
    if os.path.exists("../phones/phones.log"):
        os.remove("../phones/phones.log")
    matchua()