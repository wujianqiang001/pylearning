#!/usr/bin/env python
# coding=utf-8
def writelog(data):
    with open("access1.log","a") as f:
        f.write(data)
with open("access.log") as f:
    i = 0
    for line in f:
        writelog(line)
        i += 1
        if i>1000:
            break

import threading
threading.T
