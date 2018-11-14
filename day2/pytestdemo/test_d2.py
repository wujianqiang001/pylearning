#!/usr/bin/env python
# coding=utf-8
import pytest
def test_d():
    assert 1

def test_d2():
    assert 0

if __name__ == "__main__":
    pytest.main("--html=report.html")