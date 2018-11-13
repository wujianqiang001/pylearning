#!/usr/bin/env python
# coding=utf-8
import string, random, json, copy
a = string.ascii_lowercase
b = string.digits
c = a + b
D = {"version":123456,"add_domains":
    [{"1fdix.1bka.axy1.com":{"host":"1fdix.1bka.axy1.com","preproy":"switch","TLL":20}},
     {"rus1f.07hf.2xms.com":{"host":"rus1f.07hf.2xms.com","preproy":"switch","TLL":20}},
     {"cqphe.r7mw.nh6u.com":{"host":"cqphe.r7mw.nh6u.com","preproy":"switch","TLL":20}},
     {"sz8al.d69n.2b6o.com":{"host":"sz8al.d69n.2b6o.com","preproy":"switch","TLL":20}},
     ]}
for i in range(10):
    L = []
    for i in range(3):
        if i == 0:
            L.append("".join(random.sample(c, 5)))
        else:
            L.append("".join(random.sample(c, 4)))
    L.append("com")
    host = ".".join(L)
    
    sv = copy.copy(D["add_domains"][0]["1fdix.1bka.axy1.com"])
    sv["host"] = host
    D["add_domains"].append({host:sv})
print (D)
for s in D["add_domains"]:
    print (s)
