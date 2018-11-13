"""
a = range(10)
for i in a:
    if i%2 == 1:
        print i


b = range(10)
for i in b:
    if i%2:
        print i


c = range(10)
for i in c:
    if i%2 != 0:
        print i

d = range(10)
for i in d:
    if not i%2:
        continue
    else:
        print i
"""
_list = []
f = range(10)
for i in f:
    if i%2:
        _list.append(i)
print _list
