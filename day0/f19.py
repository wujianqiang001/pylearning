import random
p = [1,2,3,4,5,6,7,8,9]
total = {}
while True:
    a = random.sample(p, 4)
    _a = list(set(p)-set(a))
    b = random.sample(_a, 1)
    c = list(set(_a)-set(b))
    a1 = "".join([str(i) for i in a])
    b1 = "".join([str(i) for i in b])
    c1 = "".join([str(i) for i in c])
    if sorted(str(int(a1)*int(b1))) == sorted(c1):
        if (a1,b1,c1) in total:
            total[(a1,b1,c1)] = 1
        else:
            total[(a1,b1,c1)] = 0
        if len(total.keys()) > 1:
            for k in total.keys():
                print(k)
            break
