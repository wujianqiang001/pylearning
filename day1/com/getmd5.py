#!/usr/bin/env python
# coding=utf-8
import hashlib,platform
def getmd5(value):
    m = hashlib.md5()
    if platform.python_version()[0] == "3":
        m.update(value.encode("utf8"))
    else:
        m.update(value)
    return m.hexdigest()

if __name__ == "__main__":
    print(type(platform.python_version()[0]))
    g = getmd5("1111")
    print(g)