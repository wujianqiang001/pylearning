#!/usr/bin/env python
# coding=utf-8
def check(content,expection):
    for k in expection:
        if not isinstance(expection[k],dict):
            assert content[k] == expection[k]
        else:
            for k1 in expection[k]:
                if not isinstance(expection[k][k1],dict):
                    assert content[k][k1] == expection[k][k1]
                else:
                    for k2 in expection[k][k1]:
                        assert content[k][k1][k2] == expection[k][k1][k2]


def check_pytest(content,expection):
    for k in expection:
        if not isinstance(expection[k],dict):
            assert content[k] == expection[k]
        else:
            for k1 in expection[k]:
                if not isinstance(expection[k][k1],dict):
                    assert content[k][k1] == expection[k][k1]
                else:
                    for k2 in expection[k][k1]:
                        assert content[k][k1][k2] == expection[k][k1][k2]