#!/usr/bin/env python
# coding=utf-8
import copy
a = [1,2,3,4,5,6,7,8,9]
for i in a:
    b = copy.copy(a)
    b.remove(i)
    for j in b:
        c = copy.copy(b)
        c.remove(j)
        for k in c:
            d = copy.copy(c)
            d.remove(k)
            for l in d:
                e = copy.copy(d)
                e.remove(l)
                for m in e:
                    f = copy.copy(e)
                    f.remove(m)
                    s1 = "%d%d%d%d"%(j,k,l,m)
                    t1 = int(s1)*i
                    t2 = sorted(str(t1))
                    f2 = sorted([str(g) for g in f])
                    if t2 == f2:
                        print "%s*%d=%d"%(s1,i,t1)
