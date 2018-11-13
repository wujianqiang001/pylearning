d = {}
d["a"] = 1
print(d)
d["b"] = 2
d["a"] = "abc"
print(d)
for k in d:
    print(k,d[k])

for k,v in d.items():
    print(k,v)

for k in d.keys():
    print(k)

for v in d.values():
    print(v)


a = ["a","b","c"]
b = [1,2,3]
c = zip(a,b)
for i,j in c:
    print(i,j)
print(type(c))
