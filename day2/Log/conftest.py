#!/usr/bin/env python
# coding=utf-8
import pytest
@pytest.fixture(name="f",scope="module")
def openfile():
    f1 = open("test.txt","a")
    yield f1
    f1.close()