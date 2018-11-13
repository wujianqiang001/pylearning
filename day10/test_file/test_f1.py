#!/usr/bin/env python
# coding=utf-8
import pytest
def fun(f):
    f.write("bcf\n")
    return 1

def test_f(f):
    f.write("abc\n")
    assert 1 == fun(f)

if __name__ == "__main__":
    pytest.main()