#!/usr/bin/env python
# coding=utf-8
import re
ua = "Mozilla/5.0 (Linux; Android 5.0.2; MI 2 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.2454.95 Mobile Safari/537.36 LetvMobileClient_127_android"
phone = re.search("\d;\s(.+)\sBuild",ua)
print(phone.groups())