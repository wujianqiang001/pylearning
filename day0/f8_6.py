def getd():
    a = range(1,10)
    for i in a:
        for j in a:
            for k in a:
                for m in a:
                    if i not in [j,k,m] and j not in [k,m] and k != m:
                        yield [str(i),str(j),str(k),str(m)]

for i in getd():
    a = "".join(i)
    for b in range(1,10):
        if str(b) not in a:
            c  = b * int(a)
            if "".join(sorted(a+str(b)+str(c))) == "123456789":
                print(a,b,c)

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    print(indices)
    cycles = list(range(n, n-r, -1))
    print(cycles)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            print(cycles)
            print("============")
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

p = permutations(range(3))
for i in p:
    #print(i)
    pass
def tfer():
    n = 5
    while n:
        for i in reversed(range(n)):
            if n >0:
                yield i
                n -= 1
                break
            else:
                pass
        else:
            return
t = tfer()
for i in t:
    print(i)

