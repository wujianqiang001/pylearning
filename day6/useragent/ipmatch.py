#!/usr/bin/env python
# coding=utf-8
import re
p = "ip:127.0.033.134ip"
ip = re.search("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",p)
print(ip.groups())

ua = "Mozilla/5.0 (Linux; Android 4.4.2; HONOR H30-L01M Build/HonorH30-L01M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.1 baiduboxapp/8."
ua = re.search("\d;(.+)Build",ua)
if ua:
    print(ua.groups())