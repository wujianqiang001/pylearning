#!/usr/bin/env python
# coding=utf-8
import requests
def token():
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
    return uuid,login_token