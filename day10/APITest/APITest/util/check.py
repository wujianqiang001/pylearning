#!/usr/bin/env python
# coding=utf-8
def check(response,expect):
    for k in expect:
        if not isinstance(expect[k],dict):
            assert response[k] == expect[k]
        else:
            for k1 in expect[k]:
                if not isinstance(expect[k][k1],list):
                    assert response[k][k1] == expect[k][k1]
                else:
                    i = 0
                    for k2 in expect[k][k1]:
                        for k3 in k2:
                            assert response[k][k1][i][k3] == expect[k][k1][i][k3]
                        i += 1