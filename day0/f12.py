import string, random, copy
D = {"version":123456,"add_domains":
    [{"1fdix.1bka.axy1.com":{"host":"1fdix.1bka.axy1.com","preproy":"switch","TLL":0}},
     {"rus1f.07hf.2xms.com":{"host":"rus1f.07hf.2xms.com","preproy":"switch","TLL":1}},
     {"cqphe.r7mw.nh6u.com":{"host":"cqphe.r7mw.nh6u.com","preproy":"switch","TLL":2}},
     {"sz8al.d69n.2b6o.com":{"host":"sz8al.d69n.2b6o.com","preproy":"switch","TLL":3}},
     ]}

a = string.ascii_lowercase + string.digits
for i in range(10):
    L = []
    for j in range(3):
        if j == 0:
            L.append("".join(random.sample(a, 5)))
        else:
            L.append("".join(random.sample(a, 4)))
    L.append("com")
    host = ".".join(L)
    sv = copy.copy(list(D["add_domains"][0].values())[0])
    sv["host"] = host
    D["add_domains"].append({host: sv})

print(D)
for s in D["add_domains"]:
    print(s)
