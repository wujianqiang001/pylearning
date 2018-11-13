#!/usr/bin/env python
# coding=utf-8
def check(exception,content):
    for k in exception:
        assert exception[k] == content[k]