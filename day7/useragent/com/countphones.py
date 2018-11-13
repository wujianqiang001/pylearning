#!/usr/bin/env python
# coding=utf-8
def getphones():
    ps = []
    with open("../phones/phones.log") as f:
        for line in f:
            line = line.strip()
            ps.append(line)
    return ps

def getphones1():
    with open("../phones/phones.log") as f:
        for line in f:
            line = line.strip()
            yield line

def countphones():
    ps = getphones1()
    pscount = {}
    for p in ps:
        if p not in pscount:
            pscount[p] = 1
        else:
            pscount[p] += 1
    return pscount
if __name__ == "__main__":
    pscount = countphones()
    pssort = sorted(pscount.items(),key=lambda x:x[1],reverse=True)
    print(len(pssort))
    for k,v in pssort:
        print(k,v)