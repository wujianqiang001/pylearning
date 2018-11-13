#!/usr/bin/env python
# coding=utf-8
import hashlib
def getmd(value):
    md5 = hashlib.md5()
    md5.update(value.encode(encoding='utf-8'))
    signturn = md5.hexdigest()
    return signturn