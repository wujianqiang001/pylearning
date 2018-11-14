lista = [1,2,3,4,5,6,7,8,9]

def notcf (n):
    x1 =list(str(n))
    con = 0
    for i in x1:
        if x1.count(i) == 1:
            con +=1
        if con == len(x1):
            return n

for a1 in lista:
    for a2 in lista:
        if a1==a2:
            continue
        for a3 in lista:
            if a1==a3 or a2==a3:
                continue
            for a4 in lista:
                if a1==a4 or a2==a4 or a3==a4:
                    continue
                m = a1*1000+a2*100+a3*10+a4
                for k in lista:
                    if k==a1 or k==a2 or k==a3 or k==a4:
                        continue
                    n = m*k
                    m1 = str(m)
                    k1 = str(k)
                    n3 = m1 + k1+"None"+"0"
                    con=0
                    if n<10000:
                        n1 = notcf(n)
                        n2 =str(n1)
                        for i in range(4):
                            if n2[i] not in n3:
                                con +=1
                        if con ==4:
                                print("%d * %d = %s" % (m, k, n1))
