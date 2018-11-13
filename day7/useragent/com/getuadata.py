#!/usr/bin/env python
# coding=utf-8
import os,time
def writelog(data):
    with open("../sourcedata/uadatas.log","a") as f:
        f.write(data+"\n")
def getua():
    with open("../sourcedata/accesslog.log") as f:
        for line in f:
            line = line.strip()
            ua = line.split(" ")
            ua = " ".join(ua[13:-4])
            ua = ua.split("\"")[-2]
            # print(ua)
            writelog(ua)
            # break

if __name__ == "__main__":
    if os.path.exists("../sourcedata/uadatas.log"):
        os.remove("../sourcedata/uadatas.log")
    time.sleep(5)
    getua()