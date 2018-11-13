p = []
for i in range(10):
    if i%2:
        p.append(i)
print(p)

p1 = [i for i in range(10) if i%2]
print(p1)

p2 = [i for i in range(10)]
print(p2)
p3 = [str(i) for i in p2]
print(p3)
