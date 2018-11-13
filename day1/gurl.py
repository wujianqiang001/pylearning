#!/usr/bin/env python
# coding=utf-8
from PR2.day1.com.sul_1 import *
import requests,json
def writetxt(value):
    with open("report/urls_1.txt","a") as f:
        f.write(value+"\n")
def request(url):
    try:
        r = requests.get(url)
        code = {"url":url,"code":r.status_code}
    except:
        code = {"url":url,"code":502}
    return code
def main():
    with open("testcase/urls.txt") as f:
        for line in f:
            line = line.strip()
            url = skurl(line)
            writetxt(url)
            code = request(url)
            code = json.dumps(code)
            writetxt(code)
if __name__ == "__main__":
    main()
