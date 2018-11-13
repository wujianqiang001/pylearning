#!/usr/bin/env python
# coding=utf-8
import string, random, json, time,os
if os.path.exists("servernames.txt"):
    with open("servernames.txt") as f1:
        D = json.load(f1)
else:
    with open("servernames.txt", "w") as f1:
        f1.write("{\"add_domains\": [{\"1fdix.1bka.axy1.com\": \"{\\\"host\\\":\\\"1fdix.1bka.axy1.com\\\",\\\"preproy\\\":\\\"switch\\\",\\\"TLL\\\":0}\"}], \"version\": 1524295593}")
    with open("servernames.txt") as f2:
        D = json.load(f2)
D["version"] = int(time.time())
count = json.loads(((D["add_domains"][-1]).values())[0])["TLL"]
print count
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
    sv = json.loads(((D["add_domains"][0]).values())[0])
    sv["host"] = host
    sv["TLL"] = count
    D["add_domains"].append({host:json.dumps(sv)})
print D
with open("servernames.txt", "w") as f:
    json.dump(D, f)