#!/usr/bin/env python
# coding=utf-8
import pytest
from selenium import webdriver
@pytest.fixture(name="brower",scope="session")
def open_url():
    wb = webdriver.Chrome()
    wb.get("http://www.baidu.com")
    yield wb
    wb.close()