#!/usr/bin/env python
# coding=utf-8
import requests,json
header = {"User-Agent":"abc"}
r = requests.get(url="http://192.168.1.4:8801/gettradeprice1/apple")
code = r.status_code
content = r.text
# try:
#     assert code == 200
# except:
#     print("%s---------%d"%("code",code))
assert code == 200
assert json.loads(content)["price"] == 3.5
r = requests.get(url="http://192.168.1.4:8801/getua",headers=header)
print(r.text)