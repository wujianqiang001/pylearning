#!/usr/bin/env python
# coding=utf-8
from PR1.day9.com.surl import *
from PR1.day9.com.request import *
from PR1.day9.com.mysql import *
import json
def writetxt(value):
    with open("report/url.txt","a") as f:
        f.write(value+"\n")
def main():
    with open("testcase/urls.txt") as f:
        for line in f:
            line = line.strip()
            url = skurl(line)
            code = request(url)
            code = json.dumps(code)
            writetxt(code)

def test_main():
    with open("testcase/urls.txt") as f:
        for line in f:
            line = line.strip()
            url = skurl(line)
            code = request(url)
            try:
                assert code["code"] == 200
                print(".",end=" ")
            except:
                print("F",end=" ")

def getdb(sql):
    datas = []
    db = Db()
    cursor = db.selectdb(sql)
    for row in cursor:
        datas.append(row)
    return datas
if __name__ == "__main__":
    # main()
    # test_main()
    sql = "SELECT id, name, address, salary  from COMPANY"
    datas = getdb(sql)
    for d in datas:
        print(d)