#!/usr/bin/env python
# coding=utf-8
import cProfile
def numsum(a):
    if a > 0:
        return a + numsum(a-1)
    else:
        return a


