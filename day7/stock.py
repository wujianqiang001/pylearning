#!/usr/bin/env python
# coding=utf-8
import re
d = r"192.168.5.59	27/May/2018:11:25:39 +0800	`/pf?pvid=36830486-3f2d-4838-8b55-247f04c86036&ref=http%3A%2F%2F192.168.2.245%3A8080%2Fty_test%2Findex.jsp%3Fuser%3DzyTest%25E5%25BC%25A0%25E5%25AA%259B123&referrer=http%3A%2F%2F192.168.2.245%3A8080%2Fty_test%2Findex.jsp%3Fuser%3DzyTest%25E5%25BC%25A0%25E5%25AA%259B123&key=zm_K-IIie_E&v=1.7.5.0108&av=1.7.5.0108&did=b2910c9f-9a30-4c63-a830-4d711f3cf690&sid=24392cd0-b92a-427e-84fe-091635179105&f=4&qs=7&rs=3027&re=3081&os=3252&oe=3276&oi=3252&oc=3277&ls=3277&le=3310&tus=3045&tue=3045&cs=6&ce=7&je=1&id=bOlCZlNFNSA%23svB-GMpYmCk&a=3005&q=0&tid=5c25104c5a444fe7&n=index.jsp&ulabel=zyTest%E5%BC%A0%E5%AA%9B123&sh=1080&sw=1920&fp=3163&__fp=1&dr=3275&fs=3163&trflag=1001&__r=1527391545480`	1755	200	`http://192.168.2.245:8080/ty_test/index.jsp?user=zyTest%E5%BC%A0%E5%AA%9B123`	`Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36`	-	{\x22tr\x22:true,\x22tt\x22:\x22\x22,\x22charset\x22:\x22UTF-8\x22,\x2"
a = re.search("`(.+)`",d).groups()
b = re.search("\?(.+)`\t",a[0]).groups()
c = b[0]
f = c.split("&")
data = {}
for g in f:
    data[g.split("=")[0]]=g.split("=")[1]
print(data)
print(data["je"])
