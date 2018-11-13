#!/usr/bin/env python
# coding=utf-8
def writedata(dirname,filename,data):
    with open("%s/%s.log"%(dirname,filename),"a") as f:
        f.write(data+"\n")

def phonecount():
    pc = {}
    with open("phones/phones.log") as f:
        for line in f:
            line = line.strip()
            if line not in pc:
                pc[line] = 1
            else:
                pc[line] += 1
    return pc

def phonesort():
    pc = phonecount()
    pcs = sorted(pc.items(),key=lambda x:x[1],reverse=True)
    for k,v in pcs:
        writedata("phones","phonescount","%s.....%d"%(k,v))

if __name__ == "__main__":
    phonesort()
