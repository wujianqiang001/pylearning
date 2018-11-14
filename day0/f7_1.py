# -*- coding:utf-8 -*-
__author__ = 'changhongwei'

import string
import random
import copy

D = {"version":123456,"add_domains":
    [{"1fdix.1bka.axy1.com":{"host":"1fdix.1bka.axy1.com","preproy":"switch","TLL":0}},
     {"rus1f.07hf.2xms.com":{"host":"rus1f.07hf.2xms.com","preproy":"switch","TLL":1}},
     {"cqphe.r7mw.nh6u.com":{"host":"cqphe.r7mw.nh6u.com","preproy":"switch","TLL":2}},
     {"sz8al.d69n.2b6o.com":{"host":"sz8al.d69n.2b6o.com","preproy":"switch","TLL":3}},
     ]}

#定义一个函数，获取不同位数的随机数
def fun(j):
    c = string.ascii_lowercase + string.digits
    d = random.sample(c,j)
    e = ''.join(d)
    return e

#定义一个函数，插入n条数据
def insert(n):
    alist = D.get("add_domains")
    i = list(alist[-1].values())[0]["TLL"]
    for m in range(1,n+1):
        D1 = copy.copy(D)#复制一个字典
        blist = [fun(5),fun(4),fun(4),"com"]
        c = ".".join(blist)
        adict = {c:{"host":c,"preproy":"switch","TLL":m+i}}
        alist.append(adict)
        m += 1
    return alist

#把插入数据后的list放回字典中,已插入5条数据为例

D["add_domains"] = insert(5)
print(D)
