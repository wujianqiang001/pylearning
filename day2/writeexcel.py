#!/usr/bin/env python
# coding=utf-8
import requests
r = requests.get("http://www.weather.com.cn/data/sk/101010700.html")
r.encoding = "utf-8"
print(r.json())
