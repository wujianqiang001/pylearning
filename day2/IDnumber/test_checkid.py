#!/usr/bin/env python
# coding=utf-8
import IDnumcheck
import pytest

def check(idnum):
    f = IDnumcheck.idunmbertest(idnum)
    return f

idnums = [ids.strip() for ids in open("ids.txt")]
@pytest.mark.parametrize("idnum",idnums)
def test_check(idnum):
    assert check(idnum)

if __name__ == "__main__":
    pytest.main("--html=report.html")