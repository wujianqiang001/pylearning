#!/usr/bin/env python
# coding=utf-8
import allure
def fun():
    return "input"
@allure.feature("测试模块_demo1")
def test_getname(brower):
    "get name test"
    td = brower.find_element_by_id("su").tag_name
    p = fun()
    assert td == p