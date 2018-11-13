#!/usr/bin/env python
# coding=utf-8
url = "/a/live/home/abc123edfhjhrehj.ts"
u1 = url.split("/")
u2 = u1[-1]
u3 = u2.split(".")
u4 = u3[0]
if len(u4) > 10:
    u5 = u4[:10]
else:
    u5 = u4
u3[0] = u5
u3 = ".".join(u3)
u1[-1] = u3
url = "/".join(u1)
print(url)