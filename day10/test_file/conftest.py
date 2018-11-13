#!/usr/bin/env python
# coding=utf-8
import pytest
@pytest.fixture(name="f",scope="module")
def filename():
    f = open("test.txt","a")
    yield f
    f.close()