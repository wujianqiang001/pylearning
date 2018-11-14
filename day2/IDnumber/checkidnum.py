#!/usr/bin/env python
# coding=utf-8
import sys
print(sys.path)
from PR3.day2.IDnumber import IDnumcheck

with open("ids.txt") as f:
    for idnum in f:
        idnum = idnum.strip()
        print(idnum)
        IDnumcheck.main(idnum)