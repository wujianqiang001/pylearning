# !/usr/bin/env python
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
dr = webdriver.Chrome()
dr.get("http://tstmobile.gwcslife.com/NGLife/")
ActionChains(dr).key_down(Keys.CONTROL).send_keys('-').key_up(Keys.CONTROL).perform()
ActionChains(dr).key_down(Keys.CONTROL).send_keys('-').key_up(Keys.CONTROL).perform()
ActionChains(dr).key_down(Keys.CONTROL).send_keys('-').key_up(Keys.CONTROL).perform()


# def moblies():
#     with open("order1") as f:
#         mobile=[]
#
#         for i in f:
#             m=i.strip().split("|")
#             mobile.append(m)
#     return mobile
# print(moblies())
#
#
# mobiledict={}
# for elem in moblies():
#     #print(elem)
#     #key=(elem[1],elem[2])
#     #print key
#     #key = elem[0]
#     if elem[1] in mobiledict:
#         mobiledict[elem[1]]+=float(elem[4])
#         #mobiledict[key][2]+=float(elem[4])
#     else:
#         mobiledict[elem[1]]=float(elem[4])
# print(mobiledict)
# mobile=[['apple','ios','100.0','10'],['pear','android','200','20'],['apple','ios','500','50'],['pear','android','600','60']]
# mobiledict={}
# for elem in mobile:
#     print(elem)
#     key=(elem[0],elem[1])
#     if key in mobiledict:
#         mobiledict[key][0]+=float(elem[2])
#         mobiledict[key][1]+=float(elem[3])
#     else:
#         mobiledict[key]=[float(elem[2]),float(elem[3])]
# print(mobiledict)