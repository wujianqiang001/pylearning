#!/usr/bin/env python
# coding=utf-8
import re
a = "<span style=\"color:red\">腹膜后肿瘤切除术</span>"
b = re.search("<span style=\"color:(.+)\">(.+)</span>",a)
color,expection = b.groups()
assert color == "red"
assert "切除" in expection