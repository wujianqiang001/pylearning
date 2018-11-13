#!/usr/bin/env python
# coding=utf-8
import requests
header = {"Referer":"http://api.iamsaonian.com/index.php?m=Api&c=Bianli&a=shop_goods&shop_id=31&uuid=941e1aaaba585b952b62c14a3a175a61&login_token=40882d26122e53f6e91641b14f9a4b9a",
          "Cookie": "PHPSESSID=nsqkhslc56uhcaca2e5f5vgqf7"}

urls = ["http://api.iamsaonian.com/index.php?m=Api&c=Bianli&a=cart_add&uuid=941e1aaaba585b952b62c14a3a175a61&login_token=40882d26122e53f6e91641b14f9a4b9a&goods_num=8&goods_id=1195&shop_id=31",
        ]
# r = requests.get("http://api.iamsaonian.com/index.php?m=Api&c=Bianli&a=cart_add&uuid=941e1aaaba585b952b62c14a3a175a61&login_token=40882d26122e53f6e91641b14f9a4b9a&goods_num=8&goods_id=115&shop_id=31",headers=header)
# print(r.json())
# r = requests.get("http://api.iamsaonian.com/index.php?m=Api&c=Bianli&a=shop_goods&shop_id=31&uuid=941e1aaaba585b952b62c14a3a175a61&login_token=40882d26122e53f6e91641b14f9a4b9a")
# print(r.text)
# for url in urls:
#     r = requests.get(url)
#     try:
#         content = r.json()
#         assert content["errno"] == "500"
#         assert content["errmsg"] == "不存在的商品"
#         print("pass")
#     except:
#         print("fail")
#         print(content)
header = {"Content-Type": "application/x-www-form-urlencoded"}
body = {"username":"r84XtDTL5FwiP0g9w0W3rQ_c_c",
       "version":"ElF_aHf5fcoE_c",
       "device":"kDKb93msreCFRm9iFURUDyTkf2q3sLomkheybDmeacS4r014C5saHw_c_c",
       "safe_code":"YEo5sKEnyXwOam5akzneBVYTuN2Vrk7xVwQwsLfUvKB6CccMw2ZEag_c_c",
       "v":"k24nP4uRE2w_c",
       "login_type":"edi3W6UgeQ8_c",
       "skey":"T3OPE_a86674KRIUZ23O8v0P0xJqicUP4egnHDMNmRGo_c",
       "action":"dsmeJW5j048_c",
       "password":"5vRP_bgtZnmJG1PQ_bPth6rA_c_c",
       "time":"7HNxp6hZrKqhCGQztluJ3Q_c_c"}
r = requests.post("http://api.iamsaonian.com/api.php?action=login",data=body,headers=header)
content = r.json()
uuid = content["data"]["user_info"]["uuid"]
login_token = content["data"]["user_info"]["login_token"]
