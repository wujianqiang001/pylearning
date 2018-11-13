#!/usr/bin/env python
# coding=utf-8
import pytest

def test_getid(brower):
    td = brower.find_element_by_id("su").tag_name
    assert td == "a"

# if __name__ == "__main__":
#     pytest.main()