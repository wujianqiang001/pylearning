#!/usr/bin/env python
# coding=utf-8
import csv
import random
import copy
import datetime
def combindata(addrs):
    mb = []
    j = 0
    for addr in addrs:
        addrc = copy.copy(addrs)
        addrc.remove(addr)
        for ad in addrc:
            mb.append([])
            mb[j].append(addr)
            mb[j].append(ad)
            for m in range(7):
                mb[j].append(random.randint(0,1000))
            j += 1
    return mb
def writecsv(addrs):
    mb = combindata(addrs)
    with open("test.csv","w",newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(mb)
def main():
    addrs = []
    with open("addrs.txt",encoding="utf-8") as f:
        for add in f:
            addrs.append(add.strip())
    writecsv(addrs)
if __name__ == "__main__":
    starttime = datetime.datetime.now()
    main()
    endtime = datetime.datetime.now()
    print((endtime-starttime).seconds)
