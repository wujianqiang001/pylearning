#!/usr/bin/env python
# coding=utf-8
import string, random, json, time
D = {"version":123456,"add_domains":
    [{"1fdix.1bka.axy1.com":'{"host":"1fdix.1bka.axy1.com","preproy":"switch","TLL":0}'},
     {"rus1f.07hf.2xms.com":'{"host":"rus1f.07hf.2xms.com","preproy":"switch","TLL":1}'},
     {"cqphe.r7mw.nh6u.com":'{"host":"cqphe.r7mw.nh6u.com","preproy":"switch","TLL":2}'},
     {"sz8al.d69n.2b6o.com":'{"host":"sz8al.d69n.2b6o.com","preproy":"switch","TLL":3}'},
     ]}
D["version"] = int(time.time())
count = json.loads(list(D["add_domains"][-1].values())[0])["TLL"]
print (count)
c = string.ascii_lowercase + string.digits
for i in range(10):
    L = []
    for j in range(3):
        if j == 0:
            L.append("".join(random.sample(c, 5)))
        else:
            L.append("".join(random.sample(c, 4)))
    L.append("com")
    host = ".".join(L)
    count += 1
    sv = json.loads(list((D["add_domains"][0]).values())[0])
    sv["host"] = host
    sv["TLL"] = count
    D["add_domains"].append({host:json.dumps(sv)})
print (D)
for s in D["add_domains"]:
    print (s)
