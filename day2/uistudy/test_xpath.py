#!/usr/bin/env python
# coding=utf-8
def test_getname(brower):
    td = brower.find_element_by_xpath("//*[@id=\"su\"]").tag_name
    assert td == "input"