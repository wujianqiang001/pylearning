#!/usr/bin/env python
# coding=utf-8
import hashlib
def getmd5(value):
    m = hashlib.md5()
    m.update(value.encode("utf8"))
    s = m.hexdigest()
    return s

if __name__ == "__main__":
    s = getmd5("abc")
    print(s)