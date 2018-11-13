d = []
for i in range(1,4):
    d.append([])
    for j in range(1,4):
        d[i-1].append([])
        for k in range(1,4):
            d[i-1][j-1].append(k)
print(d)
print(d[1][1][1])
