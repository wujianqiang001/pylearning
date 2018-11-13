#!/usr/bin/env python
# coding=utf-8
import re
def writedata(dirname,filename,data):
    with open("%s/%s.log"%(dirname,filename),"a") as f:
        f.write(data+"\n")

def getsource():
    with open("sourcedata/access.log") as f:
        for line in f:
            line = line.strip()
            glog = line.split(" ")
            ua = " ".join(glog[13:-4])
            ua = ua.split("\"")[1]
            writedata("useragentdata","useragents",ua)

def getandroid():
    with open("useragentdata/useragents.log") as f:
        for line in f:
            line = line.strip()
            if "Android" in line:
                writedata("useragentdata","Androidua",line)

def getphone():
    with open("useragentdata/Androidua.log") as f:
        for line in f:
            line = line.strip()
            u = re.search("[\d?];\s(.+)\sBuild",line)
            if u:
                data = u.groups()[0]
                ua = re.search("[NnSs];\s(.+)",data)
                if ua:
                    data = ua.groups()[0]
                writedata("phones","phones",data)

if __name__ == "__main__":
    getphone()
