a = ["a", "b", "a", "b", "a", "c"]
b = {}
for key in a:
    if key not in b.keys():
        b[key] = 1
    else:
        b[key] += 1

print(b)

a = ["a", "b", "a", "b", "a", "c"]
c = {}
for key in a:
    count = c.get(key)
    if not count:
        count = 1
    else:
        count += 1
    c[key] = count

print(c)

a = ["a", "b", "a", "b", "a", "c"]
d = {}
for key in a:
    if key not d:
        d[key] = 1
    else:
        d[key] += 1

print(d)
